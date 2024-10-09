# Documentation de l'API Python

## Introduction

Ce script Python permet d'interagir avec une API PHP pour gérer des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) sur une base de données. Le script utilise la bibliothèque `requests` pour effectuer des requêtes HTTP vers l'API. Le code à récupérer se trouve dans `liaison_bdd.py`.

## Prérequis

Avant d'exécuter le script, assurez-vous que :

- **Python** est installé sur votre machine.
- La bibliothèque `requests` est installée. Si elle ne l'est pas, vous pouvez l'installer via Anaconda :
  ```sh
  conda install requests
  ```
- L'API PHP est déployée et accessible via l'URL fournie.

## Structure du Script

Le script contient quatre fonctions principales :

- `get_data` : Récupérer des données de la base de données.
- `add_data` : Ajouter de nouvelles données.
- `update_data` : Mettre à jour des données existantes.
- `delete_data` : Supprimer des données.

## Fonctions

### 1. Récupérer des données (GET)

**Fonction :** `get_data(table, columns='*')`

- **Paramètres :**
  - `table` : Le nom de la table d'où récupérer les données.
  - `columns` : (Optionnel) Les colonnes spécifiques à récupérer, par défaut toutes les colonnes (`*`).

**Exemple d'utilisation :**

```python
get_data("test", "alpha,beta")
```

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
```

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

## Ressources Supplémentaires

- [Documentation officielle de MySQL](https://dev.mysql.com/doc/)
- [Documentation officielle de SQL](https://www.w3schools.com/sql/)
- [Documentation officielle de Python](https://docs.python.org/3/)

---

