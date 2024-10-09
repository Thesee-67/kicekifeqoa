# Documentation de l'API Python

## Introduction

Ce script Python permet d'interagir avec une API PHP pour gérer des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) sur une base de données. Le script utilise la bibliothèque `requests` pour effectuer des requêtes HTTP vers l'API.

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

## Fonctions

### 1. Récupérer des données (GET)

**Fonction :** `get_data(table, columns='*')`

- **Paramètres :**
  - `table` : Le nom de la table d'où récupérer les données.
  - `columns` : (Optionnel) Les colonnes spécifiques à récupérer, par défaut toutes les colonnes (`*`).

**Exemple d'utilisation :**

```python
get_data("test", "alpha,beta")

### 2. Ajouter des données (POST)

**Fonction :** `add_data(table, data)`

- **Paramètres :**
  - `table` : Le nom de la table dans laquelle ajouter des données.
  - `data` : Un dictionnaire contenant les données à ajouter, où les clés sont les noms des colonnes et les valeurs sont les valeurs à insérer.

**Exemple d'utilisation :**

```python
add_data("test", {"alpha": "tic", "beta": "fax"})

