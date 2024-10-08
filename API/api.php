<?php
// Charger les informations de connexion à partir d'un fichier de configuration (optionnel) ou définir directement ici
$config = [
    'host' => 'sqlXXX.epizy.com', // Remplacez par votre hôte MySQL
    'dbname' => 'nom_de_la_base',  // Remplacez par le nom de votre base de données
    'username' => 'nom_utilisateur',  // Remplacez par votre nom d'utilisateur MySQL
    'password' => 'mot_de_passe'  // Remplacez par votre mot de passe MySQL
];

try {
    // Connexion à la base de données avec PDO
    $pdo = new PDO("mysql:host={$config['host']};dbname={$config['dbname']}", $config['username'], $config['password']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // En cas d'erreur de connexion, renvoyer une réponse avec un message d'erreur
    http_response_code(500);
    echo json_encode(["error" => "Échec de la connexion à la base de données : " . $e->getMessage()]);
    exit();
}

// Vérifier la méthode de la requête
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    try {
        // Préparer et exécuter une requête pour récupérer toutes les données d'une table (exemple : 'ma_table')
        $stmt = $pdo->prepare("SELECT * FROM ma_table"); // Remplacez par votre table
        $stmt->execute();
        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Envoyer la réponse avec les données au format JSON
        header('Content-Type: application/json');
        echo json_encode($result);
    } catch (PDOException $e) {
        // En cas d'erreur d'exécution de la requête, renvoyer un message d'erreur
        http_response_code(500);
        echo json_encode(["error" => "Erreur lors de la récupération des données : " . $e->getMessage()]);
    }
} else {
    // Si la méthode n'est pas GET, renvoyer une erreur 405 (méthode non autorisée)
    http_response_code(405);
    echo json_encode(["error" => "Méthode non autorisée. Utilisez GET."]);
}
?>
