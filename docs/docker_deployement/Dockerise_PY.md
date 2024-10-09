
# Comment Dockeriser un Projet Python dans un Environnement Conda

Ce guide vous montrera comment dockeriser un projet Python en utilisant un environnement Conda.

## Prérequis

- Docker installé sur votre machine.
- Un projet Python avec un fichier `environment.yml` pour Conda.

## Étape 1 : Créer un Dockerfile

Créez un fichier nommé `Dockerfile` à la racine de votre projet avec le contenu suivant :

```Dockerfile
# Utiliser une image de base officielle de Conda
FROM continuumio/miniconda3

# Copier le code du projet dans le conteneur
COPY .. /app
WORKDIR /app

# Installer les dépendances avec Conda
RUN conda env create -f environment.yml

# Activer l'environnement Conda
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Commande par défaut pour exécuter l'application
CMD ["python", "main.py"]
```

## Étape 2 : Créer un fichier `environment.yml`

Si vous n'avez pas déjà un fichier `environment.yml`, créez-en un à la racine de votre projet avec le contenu suivant :

```yaml
name: myenv
channels:
  - defaults
dependencies:
  - python=3.8
  # Ajoutez d'autres dépendances ici
```

## Étape 3 : Construire l'image Docker

Ouvrez un terminal et naviguez jusqu'à la racine de votre projet. Exécutez la commande suivante pour construire l'image Docker :

```sh
docker build -t my-python-app .
```

## Étape 4 : Exécuter le conteneur Docker

Une fois l'image construite, vous pouvez exécuter le conteneur avec la commande suivante :

```sh
docker run -it --rm my-python-app
```
