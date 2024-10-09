<?php
// Charger les informations de connexion
$config = [
    'host' => 'mysql-kicekifeqoa.alwaysdata.net',
    'dbname' => 'kicekifeqoa_todolist',
    'username' => '379269_admin',
    'password' => 'Kicekifeqoa123*'
];

try {
    // Connexion à la base de données avec PDO
    $pdo = new PDO("mysql:host={$config['host']};dbname={$config['dbname']}", $config['username'], $config['password']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // En cas d'erreur de connexion
    http_response_code(500);
    echo json_encode(["error" => "Échec de la connexion à la base de données : " . $e->getMessage()]);
    exit();
}

// Vérifier la méthode de la requête
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // (Récupération des données, comme montré précédemment)
    // Vérifier si un paramètre `table` a été passé
    $table = isset($_GET['table']) ? $_GET['table'] : '';
    $columns = isset($_GET['columns']) ? $_GET['columns'] : '*'; // Par défaut, toutes les colonnes

    try {
        if ($table === 'Group') {
            $stmt = $pdo->prepare("SELECT $columns FROM `Group`");
        } elseif ($table === 'Task_has_Users') {
            $stmt = $pdo->prepare("SELECT $columns FROM `Task_has_Users`");
        } else {
            http_response_code(400);
            echo json_encode(["error" => "Table non valide. Utilisez 'Group' ou 'Task_has_Users'."]);
            exit();
        }

        $stmt->execute();
        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);
        header('Content-Type: application/json');
        echo json_encode($result);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Erreur lors de la récupération des données : " . $e->getMessage()]);
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Gérer l'insertion de données
    $table = isset($_GET['table']) ? $_GET['table'] : '';

    // Lire le corps de la requête pour obtenir les données
    $data = json_decode(file_get_contents("php://input"), true);

    try {
        if ($table === 'Group') {
            // Préparer une requête d'insertion
            $stmt = $pdo->prepare("INSERT INTO `Group` (name) VALUES (:name)");
            $stmt->bindParam(':name', $data['name']); // Assurez-vous que 'name' est dans le corps de la requête
            $stmt->execute();

            // Renvoie une réponse de succès
            http_response_code(201); // Créé
            echo json_encode(["message" => "Groupe créé avec succès."]);
        } else {
            http_response_code(400);
            echo json_encode(["error" => "Table non valide. Utilisez 'Group' pour l'insertion."]);
            exit();
        }
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(["error" => "Erreur lors de l'insertion des données : " . $e->getMessage()]);
    }
} else {
    http_response_code(405);
    echo json_encode(["error" => "Méthode non autorisée. Utilisez GET ou POST."]);
}
?>
