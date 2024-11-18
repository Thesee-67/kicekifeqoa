Le schéma de la base de données inclut les tables et leurs relations. Voici une représentation visuelle du schéma de la base de données :

![Schéma de la BDD](https://media.discordapp.net/attachments/1291029541892001892/1293477123595567155/Schema_BDD_V1.png?ex=670783f1&is=67063271&hm=767e5df9882655c4076da733a5712f940734da014a6660cc7dab158da804205b&=&format=webp&quality=lossless&width=804&height=666)

## Tables de la Base de Données

### Table `Group`

- **Description** : Cette table contient les informations sur les groupes.
- **Colonnes** :
  - `id` : Identifiant unique du groupe.
  - `name` : Nom du groupe.
  - `description` : Description du groupe.

### Table `User`

- **Description** : Cette table contient les informations sur les utilisateurs.
- **Colonnes** :
  - `id` : Identifiant unique de l'utilisateur.
  - `username` : Nom d'utilisateur.
  - `email` : Adresse email de l'utilisateur.
  - `password` : Mot de passe de l'utilisateur.

### Table `Task`

- **Description** : Cette table contient les informations sur les tâches.
- **Colonnes** :
  - `id` : Identifiant unique de la tâche.
  - `title` : Titre de la tâche.
  - `description` : Description de la tâche.
  - `due_date` : Date d'échéance de la tâche.
  - `status` : Statut de la tâche (par exemple, "En cours", "Terminée").
  - `user_id` : Identifiant de l'utilisateur auquel la tâche est assignée.
  - `group_id` : Identifiant du groupe auquel la tâche est assignée.



