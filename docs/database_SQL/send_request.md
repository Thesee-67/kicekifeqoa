# Documentation pour Effectuer une Requête à une Base de Données MySQL

Ce guide vous explique comment effectuer une requête à une base de données MySQL en utilisant Python et la bibliothèque `mysql-connector-python`.

## Prérequis

- [Python](https://www.python.org/downloads/) installé sur votre machine.
- [MySQL](https://dev.mysql.com/downloads/) installé ou un serveur MySQL configuré.
- La bibliothèque `mysql-connector-python` installée. Vous pouvez l'installer en utilisant la commande suivante :
  ```sh
    conda install -c anaconda mysql-connector-python 
  ```

## Programme Python

Voici le programme Python qui effectue une requête à une base de données MySQL :

```python
from mysql.connector import (connection)

# Configuration de la connexion
config = {
    'user': '379269_admin',
    'password': 'Kicekifeqoa123*',
    'host': 'mysql-kicekifeqoa.alwaysdata.net',
    'database': 'kicekifeqoa_todolist',
}

# Connexion à la base de données
conn = connection.MySQLConnection(**config)

# Création d'un curseur
cursor = conn.cursor()

# Exécution d'une requête
query = "SELECT * FROM `Group`"
cursor.execute(query)

# Récupération des résultats
results = cursor.fetchall()

# Affichage des résultats
for row in results:
    print(row)

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
```

## Étapes

### 1. Configurer la Connexion à la Base de Données

Assurez-vous d'avoir les informations de connexion correctes pour votre base de données MySQL. Remplacez les valeurs dans le dictionnaire `config` par vos propres informations de connexion.

### 2. Installer les Dépendances

Installez la bibliothèque `mysql-connector-python` si ce n'est pas déjà fait :

```sh
conda install -c anaconda mysql-connector-python 
```

### 3. Exécuter le Programme

Enregistrez le programme dans un fichier Python, par exemple `query_mysql.py`, et exécutez-le :

```sh
python query_mysql.py
```

### 4. Vérifier les Résultats

Le programme exécute une requête SQL pour sélectionner toutes les lignes de la table `Group` et affiche les résultats. Vous pouvez vérifier les résultats dans la sortie du programme.

## Ressources Supplémentaires

- [Documentation officielle de MySQL](https://dev.mysql.com/doc/)
- [Documentation officielle de mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)
- [Documentation officielle de Python](https://docs.python.org/3/)

---
