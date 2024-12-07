# Documentation de l'API Python

## Introduction

Ce script Python permet d'interagir avec une API PHP pour gérer des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) sur une base de données. Le script utilise la bibliothèque `requests` pour effectuer des requêtes HTTP vers l'API. Le code à récupérer se trouvent dans liaison_bdd.py.

## Prérequis

Avant d'exécuter le script, assurez-vous que :

- **Python** est installé sur votre machine.
- La bibliothèque `requests` est installée. Si elle ne l'est pas, vous pouvez l'installer via anaconda :


- L'API PHP est déployée et accessible via l'URL fournie.

## Structure du Script

Le script contient quatre fonctions principales :

- `get_data` : Récupérer des données de la base de données.
- `add_data` : Ajouter de nouvelles données.
- `update_data` : Mettre à jour des données existantes.
- `delete_data` : Supprimer des données.
- `add_recup` : Ajouter de nouvelles données et recupérer l'id lié.

## Fonctions

### 1. Récupérer des données (GET)

**Fonction :** `get_data(table, columns='*')`

- **Paramètres :**
  - `table` : Le nom de la table d'où récupérer les données.
  - `columns` : (Optionnel) Les colonnes spécifiques à récupérer, par défaut toutes les colonnes (`*`).

**Exemple d'utilisation :**

```python
get_data("test", "alpha,beta")
````
### 2. Ajouter des données (POST)

**Fonction :** `add_data(table, data)`

- **Paramètres :**
  - `table` : Le nom de la table dans laquelle ajouter des données.
  - `data` : Un dictionnaire contenant les données à ajouter, où les clés sont les noms des colonnes et les valeurs sont les valeurs à insérer. Le premier mot correspond au nom de la colonne et après le `:` le mot correspond à la valeur, et il faut mettre une virgule entre chaque ajout d'information.

**Exemple d'utilisation :**

```python
add_data("test", {"alpha": "tic", "beta": "fax"})
```
### 3. Mettre à jour des données (UPDATE)

**Fonction :** `update_data(table, data, column, value)`

- **Paramètres :**
  - `table` : Le nom de la table à mettre à jour.
  - `data` : Un dictionnaire contenant les nouvelles valeurs à mettre à jour.
  - `column` : Le nom de la colonne à utiliser pour identifier la ligne à mettre à jour.
  - `value` : La valeur de la colonne pour identifier la ligne à mettre à jour.

**Exemple d'utilisation :**

```python
update_data("test", {"beta": "test"}, "beta", "fax")
````
### 4. Supprimer des données (DELETE)

**Fonction :** `delete_data(table, column, value)`

- **Paramètres :**
  - `table` : Le nom de la table d'où supprimer des données.
  - `column` : Le nom de la colonne à utiliser pour identifier la ligne à supprimer.
  - `value` : La valeur de la colonne pour identifier la ligne à supprimer.

**Exemple d'utilisation :**

```python
delete_data("test", "beta", "fax")
```

### 5. Ajouter et Récupérer un ID (POST)

**Fonction :** `add_recup(table, data)`  

- **Paramètres :**  
  - `table` : Le nom de la table où ajouter des données.  
  - `data` : Un dictionnaire contenant les colonnes et leurs valeurs à insérer.  

**Exemple d'utilisation :**  

```python
add_recup("test", {"alpha": "tic", "beta": "fax"})
```
Retour :

    Succès :
        L'ID généré par l'insertion sera retourné sous forme de dictionnaire.

    Erreur :
        Un message d'erreur sera affiché en cas de problème lors de l'ajout.

Exemple réel :

````python
data = {"name": "John Doe", "email": "john.doe@example.com"}
generated_id = add_recup("Users", data)
print(f"Nouvel ID : {generated_id}")
````

### 6. Compter des Occurrences (COUNT)

**Fonction :** `count_data(table, filter_column, filter_value)`  

- **Paramètres :**  
  - `table` : Le nom de la table dans laquelle effectuer le comptage.  
  - `filter_column` : Le nom de la colonne utilisée pour filtrer les données.  
  - `filter_value` : La valeur de la colonne utilisée pour le filtre.  

**Exemple d'utilisation :**  

```python
count_data("Group", "name", "ouioui")
```

Retour :

    Succès :
        Type : Dictionnaire
        Contenu : Nombre total d'occurrences correspondant au filtre.
        Exemple :
        
```json
{
  "status": "success",
  "count": 3
}
```

Exemple réel :

```python
result = count_data("Group", "name", "ouioui")
print(f"Nombre total : {result}")
```

# Comment utiliser le code

Lorsque vous souhaitez utiliser tout ou partie du code, suivez les étapes ci-dessous :

### 1. Prenez les imports nécessaires :

```python
import requests
import json
```
### 2. Définissez l'URL de l'API :

```python
url = "http://kicekifeqoa.alwaysdata.net/api.php"
```
### 3. Choisissez la fonction (définition) qui vous intéresse :

- Récupérer des données (GET) : `get_data`
- Ajouter des données (POST) : `add_data`
- Mettre à jour des données (UPDATE) : `update_data`
- Supprimer des données (DELETE) : `delete_data`

### 4. Utilisez la commande correspondante pour l'action que vous souhaitez effectuer.

**Exemple pour ajouter des données :**

```python
add_data("nom_de_la_table", {"colonne1": "valeur1", "colonne2": "valeur2"})
```







