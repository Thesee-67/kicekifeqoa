# Code

# Documentation pour la Partie Graphique du Projet To-Do List

## 1. **Aperçu de la Structure du Projet**

L'interface graphique du projet To-Do List est construite en utilisant QML et interagit avec la logique Python pour gérer les tâches. Les composants principaux du projet sont :

![arboresence_QT](https://i.imgur.com/5MmmlHH.png)

### Fichiers QML Principaux (Couche d'Interface) :
- **`App.qml`** : La fenêtre principale qui affiche un tableau de tâches organisé en quatre colonnes. Chaque colonne représente une priorité de tâche différente (Urgent, Moyen, Basse, Terminée). Ce fichier contient aussi des boutons pour ajouter, modifier et supprimer des tâches.
- **`PopupCreateTask.qml`** : L'interface pour ajouter une nouvelle tâche.
- **`PopupDeleteTask.qml`** : L'interface pour supprimer une tâche existante.
- **`PopupUpdateTask.qml`** : L'interface pour modifier une tâche.

### Logique Backend (Gestion des Tâches) :
- Les fichiers QML envoient des signaux vers des gestionnaires de tâches en Python situés dans les fichiers du répertoire `taskhandlers`. Chaque popup (ajout, suppression, modification) déclenche l'envoi d'un signal vers un fichier Python correspondant pour effectuer les actions nécessaires.

### Fonctionnement Global :
- **`start_frontend.py`** : Ce fichier lance l'application en chargeant `App.qml`, la fenêtre principale qui contient toutes les tâches.
- **`App.qml`** : Ce fichier affiche les tâches sous forme de cartes dans un tableau de 4 colonnes, chacune représentant un niveau de priorité. Chaque carte contient des informations telles que le nom, l'ID, la date de fin, et une case à cocher pour marquer si la tâche est terminée ou non.
  - **Pour chaque carte :**
    - Un bouton de modification ouvre `PopupUpdateTask.qml`.
    - Un bouton de suppression ouvre `PopupDeleteTask.qml`.
  - En bas de chaque colonne, il y a un bouton pour ajouter une nouvelle tâche, qui ouvre `PopupCreateTask.qml`.
  
- **Interaction Backend :** 
    - Chaque popup (ajout, suppression, modification) envoie des signaux aux gestionnaires de tâches respectifs situés dans le répertoire `taskhandlers` :
        - **Ajout de tâche** : `PopupCreateTask.qml` envoie les informations de la nouvelle tâche à `task_handler_Pcreate.py`.
        - **Suppression de tâche** : `PopupDeleteTask.qml` envoie l'ID de la tâche à supprimer à `task_handler_Pdelete.py`.
        - **Modification de tâche** : `PopupUpdateTask.qml` envoie les informations mises à jour à `task_handler_Pupdate.py`.

## 2. **Détails des Fichiers Taskhandlers**

Les **popups** (comme `PopupCreateTask.qml`, `PopupUpdateTask.qml`, et `PopupDeleteTask.qml`) servent d'interfaces utilisateur pour ajouter, modifier ou supprimer des tâches. Ces popups envoient d'abord des informations vers `App.qml`, qui, à son tour, transmet les données aux **gestionnaires de tâches** (taskhandlers) dans les fichiers Python correspondants. Voici un aperçu détaillé de chaque gestionnaire de tâches :

### a. **Fichier `task_handler_Pcreate.py`** : Gestionnaire pour l'ajout de tâches
Lorsque l'utilisateur ouvre le popup d'ajout (`PopupCreateTask.qml`) et valide les informations, les données sont envoyées à `App.qml`. Celui-ci transmet ensuite les données à `task_handler_Pcreate.py` via des signaux. Ce gestionnaire se charge de :

- **Récupérer les informations de la tâche** (nom, priorité, étiquettes, utilisateurs, dates de début et de fin, etc.) envoyées depuis l'interface utilisateur.
- **Créer la nouvelle tâche** dans la base de données ou tout autre stockage utilisé.
- **Envoyer une réponse de confirmation** à `App.qml` pour indiquer que l'ajout a été effectué avec succès. Ensuite, `App.qml` met à jour la liste des tâches affichées.

**Processus :**
1. Le popup d'ajout envoie les signaux des informations de la tâche à `App.qml`.
2. `App.qml` transmet les signaux à `task_handler_Pcreate.py`.
3. Le gestionnaire traite les données et ajoute la tâche.

### b. **Fichier `task_handler_Pupdate.py`** : Gestionnaire pour la modification de tâches
Lorsqu'un utilisateur modifie une tâche via le popup de modification (`PopupUpdateTask.qml`), les informations mises à jour sont d'abord envoyées à `App.qml`. Ensuite, `App.qml` transmet ces informations à `task_handler_Pupdate.py`. Ce gestionnaire se charge de :

- **Recevoir les données mises à jour** de la tâche (nom, priorité, étiquettes, utilisateurs, dates, etc.).
- **Modifier la tâche existante** en fonction des informations fournies dans l'interface.
- **Confirmer la mise à jour** en renvoyant une réponse à `App.qml` pour rafraîchir l'affichage des tâches.

**Processus :**
1. Le popup de modification envoie les nouvelles informations de la tâche à `App.qml`.
2. `App.qml` transfère ces informations à `task_handler_Pupdate.py`.
3. Le gestionnaire met à jour la tâche dans la base de données.

### c. **Fichier `task_handler_Pdelete.py`** : Gestionnaire pour la suppression de tâches
Lorsque l'utilisateur choisit de supprimer une tâche à travers le popup de suppression (`PopupDeleteTask.qml`), l'ID de la tâche à supprimer est envoyé à `App.qml`, qui redirige ensuite cette information vers `task_handler_Pdelete.py`. Ce gestionnaire se charge de :

- **Recevoir l'ID de la tâche à supprimer**.
- **Supprimer la tâche** correspondante de la base de données.
- **Notifier `App.qml`** une fois la tâche supprimée afin de mettre à jour l'affichage des tâches.

**Processus :**
1. Le popup de suppression envoie l'ID de la tâche à supprimer à `App.qml`.
2. `App.qml` transfère cet ID à `task_handler_Pdelete.py`.
3. Le gestionnaire supprime la tâche de la base de données et confirme l'action.

### d. **Fichier `task_handler_AppRead.py`** : Gestionnaire de lecture des tâches
Ce fichier est utilisé pour **récupérer les tâches** et les envoyer à `App.qml`, qui les affiche dans les différentes colonnes du tableau. Ce gestionnaire est appelé à chaque fois qu'une modification est effectuée (ajout, suppression ou mise à jour) afin de rafraîchir les données affichées.

- **Fetch tasks** : Ce gestionnaire communique avec la base de données pour extraire toutes les tâches et les renvoie à `App.qml`.
- **Organisation des tâches** : Les tâches sont ensuite organisées par `App.qml` en fonction de leur priorité et leur statut (terminée ou non).

**Processus :**
1. Après chaque action (ajout, modification, suppression), `task_handler_AppRead.py` est invoqué pour récupérer toutes les tâches.
2. Les tâches sont renvoyées à `App.qml` pour être affichées dans les colonnes correspondantes.

## 3. **Détails des Fichiers QML**

Les fichiers QML définissent l'interface utilisateur et gèrent les interactions visuelles avec les tâches (ajout, modification, suppression). Chaque popup ou composant est responsable d'une fonctionnalité spécifique et interagit avec le backend Python via les signaux. Voici un aperçu détaillé de chaque fichier QML :

### a. **`App.qml`** : La Fenêtre Principale
Ce fichier représente la fenêtre principale de l'application où toutes les tâches sont affichées dans un tableau à quatre colonnes. Chaque colonne correspond à un niveau de priorité (Urgent, Moyen, Basse, Terminée), et chaque tâche est représentée sous forme de carte.

- **Composants principaux :**
  - **GridLayout** : Organise les tâches en quatre colonnes, chaque colonne représentant une priorité spécifique.
  - **ListView** : Utilisé pour afficher les tâches sous forme de cartes dans chaque colonne.
  - **Delegate** : Chaque tâche est représentée par une carte (un rectangle) qui contient des informations comme le nom, l'ID, la priorité, la date de fin, et une case à cocher pour marquer si la tâche est terminée.
  - **Boutons d'action** :
    - **Bouton de modification** (icône "🖌️") : Permet de modifier la tâche en ouvrant `PopupUpdateTask.qml`.
    - **Bouton de suppression** (icône "🗑️") : Permet de supprimer la tâche en ouvrant `PopupDeleteTask.qml`.
    - **Bouton d'ajout** (icône "+") : Permet d'ajouter une nouvelle tâche en ouvrant `PopupCreateTask.qml`.

### b. **`PopupCreateTask.qml`** : Popup pour Créer une Tâche

Ce fichier QML définit l'interface pour l'ajout d'une nouvelle tâche. L'utilisateur peut entrer les informations de la tâche, comme son nom, sa priorité, les étiquettes, les utilisateurs, et les dates.

- **Composants principaux** :
  - **TextField** : Champs de texte pour entrer le nom de la tâche, la date de début, et la date de fin.
  - **Slider** : Permet de sélectionner la priorité de la tâche (Urgente, Moyenne, Basse).
  - **RoundButton** : Boutons pour ajouter/supprimer des étiquettes et des utilisateurs.
  - **CheckBox** : Case à cocher pour marquer la tâche comme terminée.
  - **Bouton de validation (✓)** : Valide l'ajout de la tâche et ferme le popup après envoi des données au backend via les signaux.

### c. **`PopupDeleteTask.qml`** : Popup pour Supprimer une Tâche
Ce fichier QML gère l'interface pour confirmer la suppression d'une tâche. L'utilisateur voit le nom de la tâche à supprimer et doit valider ou annuler l'action.

- **Composants principaux** :
  - **Text** : Affiche le nom de la tâche à supprimer.
  - **RoundButton** : Boutons pour confirmer (✓) ou annuler (❌) la suppression.


### d. **`PopupUpdateTask.qml`** : Popup pour Modifier une Tâche
Ce fichier gère l'interface de modification d'une tâche existante. L'utilisateur peut changer le nom, la priorité, les étiquettes, les utilisateurs, et les dates de la tâche.

- **Composants principaux** :
  - **TextField** : Champs de texte pour entrer le nom de la tâche, la date de début, et la date de fin.
  - **Slider** : Permet de modifier la priorité de la tâche.
  - **RoundButton** : Boutons pour ajouter/supprimer des étiquettes et des utilisateurs.
  - **CheckBox** : Case à cocher pour marquer la tâche comme terminée.
  - **Bouton de validation (✓)** : Valide la modification de la tâche et ferme le popup après envoi des données.