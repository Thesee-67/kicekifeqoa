<?php
// Clé de chiffrement utilisée pour le fichier de configuration
$key = hash('sha256', 'fd7fbf262118bc9631193efdab5e33adf88530610f7bc8bc7c19f7a3ca76f34d', true);

// Chemin vers le fichier de configuration chiffré
$encryptedFile = __DIR__ . '/../db_config.enc';

// Chargement de la configuration de la base de données
if (file_exists($encryptedFile)) {
    $encryptedData = file_get_contents($encryptedFile);

    // Récupérer l'IV et les données chiffrées
    $iv = substr($encryptedData, 0, 16);
    $ciphertext = substr($encryptedData, 16);

    // Déchiffrer les données
    $decryptedData = openssl_decrypt($ciphertext, 'aes-256-cbc', $key, OPENSSL_RAW_DATA, $iv);

    if ($decryptedData === false || empty($decryptedData)) {
        http_response_code(500);
        echo json_encode(["error" => "Erreur de déchiffrement des données."]);
        exit();
    }

    $config = json_decode($decryptedData, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        http_response_code(500);
        echo json_encode(["error" => "Erreur dans les données JSON : " . json_last_error_msg()]);
        exit();
    }

    try {
        // Connexion à la base de données
        $pdo = new PDO(
            "mysql:host={$config['host']};dbname={$config['dbname']};charset=utf8mb4",
            $config['username'],
            $config['password']
        );
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Connexion à la base de données échouée : " . $e->getMessage()]);
        exit();
    }
} else {
    http_response_code(500);
    echo json_encode(["error" => "Fichier de configuration introuvable."]);
    exit();
}

// Gestion des requêtes API
$requestMethod = $_SERVER['REQUEST_METHOD'];
try {
    switch ($requestMethod) {
        case 'GET':
            handleGet($pdo);
            break;
        case 'POST':
            handlePost($pdo);
            break;
        case 'DELETE':
            handleDelete($pdo);
            break;
        case 'COUNT':
            handleCount($pdo);
            break;
        default:
            http_response_code(405);
            echo json_encode(["error" => "Méthode non autorisée."]);
    }
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(["error" => "Erreur serveur : " . $e->getMessage()]);
}

// Gestion des requêtes GET
function handleGet($pdo) {
    $table = $_GET['table'] ?? null;
    $columns = $_GET['columns'] ?? '*';
    $filterColumn = $_GET['filter_column'] ?? null;
    $filterValue = $_GET['filter_value'] ?? null;

    if (!$table) {
        http_response_code(400);
        echo json_encode(["error" => "Nom de table manquant."]);
        return;
    }

    $query = "SELECT $columns FROM `$table`";
    $params = [];

    if ($filterColumn && $filterValue !== null) {
        $query .= " WHERE `$filterColumn` = :filterValue";
        $params['filterValue'] = $filterValue;
    }

    try {
        $stmt = $pdo->prepare($query);
        $stmt->execute($params);
        $result = $stmt->fetchAll();
        header('Content-Type: application/json');
        echo json_encode($result);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Erreur lors de la récupération des données : " . $e->getMessage()]);
    }
}

// Gestion des requêtes POST
function handlePost($pdo) {
    $data = json_decode(file_get_contents("php://input"), true);
    $table = $data['table'] ?? null;
    $action = $data['action'] ?? null;

    if (!$table || !$action) {
        http_response_code(400);
        echo json_encode(["error" => "Paramètres manquants : 'table' et 'action'."]);
        return;
    }

    if ($action === 'insert') {
        $columns = implode(", ", array_keys($data['data']));
        $placeholders = implode(", ", array_fill(0, count($data['data']), '?'));
        $query = "INSERT INTO `$table` ($columns) VALUES ($placeholders)";

        try {
            $stmt = $pdo->prepare($query);
            $stmt->execute(array_values($data['data']));
            echo json_encode(["message" => "Données ajoutées avec succès."]);
        } catch (PDOException $e) {
            http_response_code(500);
            echo json_encode(["error" => "Erreur lors de l'insertion : " . $e->getMessage()]);
        }
    } elseif ($action === 'update') {
        $set = implode(", ", array_map(fn($col) => "$col = ?", array_keys($data['data'])));
        $query = "UPDATE `$table` SET $set WHERE `{$data['column']}` = ?";
        try {
            $stmt = $pdo->prepare($query);
            $stmt->execute(array_merge(array_values($data['data']), [$data['value']]));
            echo json_encode(["message" => "Données mises à jour avec succès."]);
        } catch (PDOException $e) {
            http_response_code(500);
            echo json_encode(["error" => "Erreur lors de la mise à jour : " . $e->getMessage()]);
        }
    } else {
        http_response_code(400);
        echo json_encode(["error" => "Action inconnue."]);
    }
}

// Gestion des requêtes DELETE
function handleDelete($pdo) {
    $data = json_decode(file_get_contents("php://input"), true);
    $table = $data['table'] ?? null;
    $column = $data['column'] ?? null;
    $value = $data['value'] ?? null;

    if (!$table || !$column || !$value) {
        http_response_code(400);
        echo json_encode(["error" => "Paramètres manquants : 'table', 'column', 'value'."]);
        return;
    }

    $query = "DELETE FROM `$table` WHERE `$column` = ?";
    try {
        $stmt = $pdo->prepare($query);
        $stmt->execute([$value]);
        echo json_encode(["message" => "Données supprimées avec succès."]);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Erreur lors de la suppression : " . $e->getMessage()]);
    }
}

// Gestion des requêtes COUNT
function handleCount($pdo) {
    $table = $_GET['table'] ?? null;
    $filterColumn = $_GET['filter_column'] ?? null;
    $filterValue = $_GET['filter_value'] ?? null;

    if (!$table || !$filterColumn) {
        http_response_code(400);
        echo json_encode(["error" => "Paramètres manquants : 'table' et 'filter_column'."]);
        return;
    }

    $query = "SELECT COUNT(*) AS count FROM `$table` WHERE `$filterColumn` = :filterValue";
    try {
        $stmt = $pdo->prepare($query);
        $stmt->execute(['filterValue' => $filterValue]);
        $result = $stmt->fetch();
        header('Content-Type: application/json');
        echo json_encode($result);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Erreur lors du comptage : " . $e->getMessage()]);
    }
}
