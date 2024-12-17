TaskHandlerLogin Class
======================

.. class:: TaskHandlerLogin(engine)

    Cette classe gère le processus d'authentification des utilisateurs en vérifiant les informations de connexion et en chargeant l'interface principale après une authentification réussie.

    :param engine: L'instance de `QQmlApplicationEngine` utilisée pour charger les interfaces QML.
    :type engine: PySide6.QtQml.QQmlApplicationEngine

    Signals:
    --------
    - **loginSuccess (int)** : Signal émis après une connexion réussie avec l'ID de l'utilisateur en paramètre.
    - **loginPasswdFail** : Signal émis lorsque le mot de passe est incorrect.
    - **loginEmailFail** : Signal émis lorsque l'email est introuvable.

    Methods:
    --------

    .. method:: verify_password(stored_password, provided_password)

        Compare le mot de passe fourni avec le hash stocké.

        :param stored_password: Le mot de passe haché stocké.
        :type stored_password: bytes
        :param provided_password: Le mot de passe fourni par l'utilisateur.
        :type provided_password: str
        :return: `True` si le mot de passe est valide, `False` sinon.
        :rtype: bool

    .. method:: checkCredentials(email, password)

        Vérifie les informations d'identification de l'utilisateur (email et mot de passe). Si l'authentification réussit, charge l'interface `App.qml` et récupère les tâches de l'utilisateur.

        :param email: L'email de l'utilisateur.
        :type email: str
        :param password: Le mot de passe de l'utilisateur.
        :type password: str

        Signals émis :
        - `loginSuccess(int)`: En cas de succès, transmet l'ID de l'utilisateur.
        - `loginPasswdFail`: Si le mot de passe est incorrect.
        - `loginEmailFail`: Si l'email est introuvable.

        Exemple d'utilisation :

        .. code-block:: python

            task_handler = TaskHandlerLogin(engine)
            task_handler.loginSuccess.connect(on_login_success)
            task_handler.loginPasswdFail.connect(on_password_fail)
            task_handler.loginEmailFail.connect(on_email_fail)

            task_handler.checkCredentials("user@example.com", "password123")

    .. method:: get_user_id()

        Retourne l'ID de l'utilisateur après une connexion réussie.

        :return: L'ID de l'utilisateur.
        :rtype: int or None
