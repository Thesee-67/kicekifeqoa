# Documentation pour l'Envoi de Données vers MongoDB

Ce guide vous explique comment envoyer des données vers une base de données MongoDB en utilisant Python et la bibliothèque `pymongo`.

## Prérequis

- [Python](https://www.python.org/downloads/) installé sur votre machine.
- [MongoDB](https://www.mongodb.com/try/download/community) installé ou un cluster MongoDB Atlas configuré.
- [Conda](https://docs.conda.io/en/latest/miniconda.html) installé.

## Programme Python

Voici le programme Python qui envoie des données vers une base de données MongoDB :

```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

# URI de connexion à MongoDB
uri = "mongodb+srv://evaaaaanh:nONBELsIvoWWJSnJ@cluster0.iptlw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Créez un nouveau client et connectez-vous au serveur
client = MongoClient(uri, server_api=ServerApi('1'))

# Nom de la base de données et de la collection
db_name = 'BDD'
collection_name = 'Kanban'

# Sélectionnez la base de données et la collection
db = client[db_name]
collection = db[collection_name]

# Exemple de document à insérer
document = {
    'cardID': '1',
    'user': '1',
    'colonnes': '1',
    'date': datetime.now(),
    'urgence': '1',
}

# Insérez le document dans la collection
try:
    result = collection.insert_one(document)
    print(f"Document inséré avec l'ID: {result.inserted_id}")
except Exception as e:
    print(f"Erreur lors de l'insertion du document: {e}")

# Envoyez un ping pour confirmer une connexion réussie
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Erreur de connexion à MongoDB: {e}")

# Fermez la connexion
client.close()
```
## Étapes

### 1. Configurer la connexion à MongoDB

Assurez-vous d'avoir une URI de connexion valide pour votre cluster MongoDB. Remplacez la valeur de `uri` dans le programme par votre propre URI de connexion.

### 2. Installer les dépendances avec Conda

Créez un environnement Conda et installez les dépendances nécessaires :

```sh
# Créez un nouvel environnement Conda
conda create -n myenv python=3.9

# Activez l'environnement Conda
conda activate myenv

# Installez la bibliothèque pymongo
conda install -c anaconda pymongo
```

### 3. Exécuter le programme

Enregistrez le programme dans un fichier Python, par exemple `send_to_mongodb.py`, et exécutez-le :

```sh
python send_to_mongodb.py
```

## Ressources supplémentaires

- [Documentation officielle de MongoDB](https://docs.mongodb.com/)
- [Documentation officielle de pymongo](https://pymongo.readthedocs.io/en/stable/)
- [Documentation officielle de Python](https://docs.python.org/3/)

---
