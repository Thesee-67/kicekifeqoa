from CRUD.Group.Create import create_group
from CRUD.Group.Delete import delete_group
from CRUD.Group.Read import read_group
from CRUD.Group.Update import update_group

from CRUD.Subtask.Create import create_subtask
from CRUD.Subtask.Delete import delete_subtask
from CRUD.Subtask.Read import read_subtask
from CRUD.Subtask.Update import update_subtask

from CRUD.Task.Create import create_task, create_sub_task
from CRUD.Task.Delete import delete_task
from CRUD.Task.Read import read_task
from CRUD.Task.Update import update_task

from CRUD.Users.Create import create_user
from CRUD.Users.Delete import delete_user
from CRUD.Users.Read import read_user
from CRUD.Users.Update import update_user

from utils import connect_db, refresh_data, link_user_to_task, validate_input


def main():
    # Connexion à la base de données
    conn = connect_db()

    print("Bienvenue dans l'application de gestion de tâches kicekifekoa")
    print("Veuillez choisir une option :")
    print("1. Créer une tâche")
    print("2. Lire une tâche")
    print("3. Mettre à jour une tâche")
    print("4. Supprimer une tâche")
    print("5. Créer une sous-tâche")
    print("6. Lire une sous-tâche")
    print("7. Mettre à jour une sous-tâche")
    print("8. Supprimer une sous-tâche")
    print("9. Liaison utilisateur avec une tâche")
    print("10. Refresh - Mise à jour des informations locales")
    print("11. Quitter")

    choice = input("Choisissez une option : ")

    # Traitement des différentes options
    if choice == "1":
        create_task(conn)
    elif choice == "2":
        read_task(conn)
    elif choice == "3":
        update_task(conn)
    elif choice == "4":
        delete_task(conn)
    elif choice == "5":
        create_sub_task(conn)
    elif choice == "6":
        read_subtask(conn)
    elif choice == "7":
        update_subtask(conn)
    elif choice == "8":
        delete_subtask(conn)
    elif choice == "9":
        user_id = input("Entrez l'identifiant de l'utilisateur : ")
        task_id = input("Entrez l'identifiant de la tâche : ")
        link_user_to_task(conn, user_id, task_id)
    elif choice == "10":
        refresh_data(conn)
    elif choice == "11":
        print("Merci d'avoir utilisé kicekifekoa. À bientôt !")
        conn.close()
        exit()
    else:
        print("Option non valide, veuillez réessayer.")

    # Relancer le menu principal
    main()


if __name__ == "__main__":
    main()
