<?php
var_dump($_GET); // Pour le débogage

// Clé de chiffrement utilisée pour chiffrer le fichier
$key = hash('sha256', 'fd7fbf262118bc9631193efdab5e33adf88530610f7bc8bc7c19f7a3ca76f34d', true); // Clé de 32 octets

// Chemin vers le fichier chiffré
$encryptedFile = __DIR__ . '/../db_config.enc';

if (file_exists($encryptedFile)) {
    // Lire et décoder le contenu du fichier chiffré
    $encryptedData = file_get_contents($encryptedFile);

    // Séparer l'IV et les données chiffrées
    $iv = substr($encryptedData, 0, 16); // Les 16 premiers octets sont l'IV
    $ciphertext = substr($encryptedData, 16); // Le reste est le texte chiffré

    // Déchiffrer les données
    $decryptedData = openssl_decrypt($ciphertext, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);

    if ($decryptedData === false) {
        http_response_code(500);
        echo json_encode(["error" => "Échec du déchiffrement : " . openssl_error_string()]);
        exit();
    }

    // Vérifiez si $decryptedData est bien une chaîne et contient des données
    if (empty($decryptedData)) {
        http_response_code(500);
        echo json_encode(["error" => "Les données déchiffrées sont vides."]);
        exit();
    }

    // Convertir les données déchiffrées en tableau PHP
    $config = json_decode($decryptedData, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        http_response_code(500);
        echo json_encode(["error" => "Erreur JSON : " . json_last_error_msg()]);
        exit();
    }

    try {
        // Connexion à la base de données avec PDO
        $pdo = new PDO("mysql:host={$config['host']};dbname={$config['dbname']}", $config['username'], $config['password']);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Échec de la connexion à la base de données : " . $e->getMessage()]);
        exit();
    }
} else {
    http_response_code(500);
    echo json_encode(["error" => "Erreur interne, fichier de configuration manquant."]);
    exit();
}

function encrypt_data($data) {
    $key2 = hex2bin("ad7f252117bc9633183efaae5e33aaf08530610f7bc8bc7e19f1a3ca96f64e00"); // Clé de chiffrement
    $iv = '0123456789abcdef'; // IV fixe
    $encryptedData = openssl_encrypt($data, 'aes-256-cbc', $key2, OPENSSL_RAW_DATA, $iv);
    return base64_encode($encryptedData);
}

function decrypt_data($data) {
    $key3 = hex2bin("ad7f252117bc9633183efaae5e33aaf08530610f7bc8bc7e19f1a3ca96f64e00"); // Clé de chiffrement
    $iv = '0123456789abcdef'; // IV fixe
    $decodedData = base64_decode($data);
    $decryptedData = openssl_decrypt($decodedData, 'aes-256-cbc', $key3, OPENSSL_RAW_DATA, $iv);

    if ($decryptedData === false) {
        error_log("Erreur de déchiffrement : " . openssl_error_string());
        return false;
    }
    return $decryptedData;
}


$requestData = file_get_contents("php://input");
$decryptedData = decrypt_data($requestData);

if ($decryptedData === false) {
    http_response_code(500);
    echo json_encode(["error" => "Échec du déchiffrement de la requête."]);
    exit();
}

$data = json_decode($decryptedData, true);
if (json_last_error() !== JSON_ERROR_NONE) {
    http_response_code(400);
    echo json_encode(["error" => "Erreur JSON : " . json_last_error_msg()]);
    exit();
}

$requestMethod = $_SERVER['REQUEST_METHOD'];
switch ($requestMethod) {
    case 'GET':
        $response = handleGet($pdo);
        break;
    case 'POST':
        $response = handlePost($pdo, $data);
        break;
    case 'DELETE':
        $response = handleDelete($pdo, $data);
        break;
    case 'COUNT':
        $response = handleCount($pdo);
        break;
    default:
        http_response_code(405);
        $response = ["error" => "Méthode non autorisée. Utilisez GET, POST, DELETE ou COUNT."];
}

header('Content-Type: application/json');
echo encrypt_data(json_encode($response));

// Définition des fonctions pour chaque requête

function handleGet($pdo) {
    $table = $_GET['table'] ?? null;
    $columns = $_GET['columns'] ?? '*';
    $filterColumn = $_GET['filter_column'] ?? null;
    $filterValue = $_GET['filter_value'] ?? null;
    $joinTables = $_GET['join_table'] ?? null;
    $joinConditions = $_GET['join_condition'] ?? null;

    if ($table) {
        $query = "SELECT $columns FROM `$table`";
        if ($joinTables && $joinConditions) {
            $joinTablesArray = explode(",", $joinTables);
            $joinConditionsArray = explode(",", $joinConditions);
            foreach ($joinTablesArray as $index => $joinTable) {
                $query .= " JOIN `$joinTable` ON $joinConditionsArray[$index]";
            }
        }
        if ($filterColumn && $filterValue !== null) {
            $query .= " WHERE $filterColumn = :filterValue";
            $stmt = $pdo->prepare($query);
            $stmt->bindValue(':filterValue', is_numeric($filterValue) ? (int)$filterValue : $filterValue, PDO::PARAM_STR);
        } else {
            $stmt = $pdo->prepare($query);
        }
        try {
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            http_response_code(500);
            return ["error" => "Erreur lors de la récupération des données : " . $e->getMessage()];
        }
    } else {
        http_response_code(400);
        return ["error" => "Nom de table manquant."];
    }
}

function handlePost($pdo, $data) { // Recevoir $data ici
    $table = $data['table'] ?? null;
    $action = $data['action'] ?? null;

    if ($table && $action) {
        if ($action === 'insert') {
            $columns = implode(", ", array_keys($data['data']));
            $placeholders = implode(", ", array_fill(0, count($data['data']), '?'));
            $stmt = $pdo->prepare("INSERT INTO `$table` ($columns) VALUES ($placeholders)");
            $stmt->execute(array_values($data['data']));
            return ["message" => "Données ajoutées avec succès."];
        } elseif ($action === 'update') {
            $set = [];
            foreach ($data['data'] as $column => $value) {
                $set[] = "$column = ?";
            }
            $set = implode(", ", $set);
            $column = $data['column'];
            $value = $data['value'];
            $stmt = $pdo->prepare("UPDATE `$table` SET $set WHERE $column = ?");
            $stmt->execute(array_merge(array_values($data['data']), [$value]));
            return ["message" => "Données mises à jour avec succès."];
        } else {
            http_response_code(400);
            return ["error" => "Action non reconnue."];
        }
    } else {
        http_response_code(400);
        return ["error" => "Nom de table ou action manquante."];
    }
}

function handleDelete($pdo, $data) { // Recevoir $data ici
    $table = $data['table'] ?? null;
    $column = $data['column'] ?? null;
    $value = $data['value'] ?? null;

    if ($table && $column && $value) {
        $stmt = $pdo->prepare("DELETE FROM `$table` WHERE $column = ?");
        $stmt->execute([$value]);
        return ["message" => "Données supprimées avec succès."];
    } else {
        http_response_code(400);
        return ["error" => "Table, colonne ou valeur manquante."];
    }
}

function handleCount($pdo) {
    $table = $_GET['table'] ?? null;
    $filterColumn = $_GET['filter_column'] ?? null;
    $filterValue = $_GET['filter_value'] ?? null;

    if ($table && $filterColumn) {
        $query = "SELECT COUNT(*) AS count FROM `$table` WHERE $filterColumn = :filterValue";
        $stmt = $pdo->prepare($query);
        $stmt->bindValue(':filterValue', $filterValue);

        try {
            $stmt->execute();
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            http_response_code(500);
            return ["error" => "Erreur lors du comptage des données : " . $e->getMessage()];
        }
    } else {
        http_response_code(400);
        return ["error" => "Nom de table ou colonne de filtre manquante."];
    }
}
?>
