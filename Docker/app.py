import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def maintenance_message():
    return 'Bonjour, cette application est en cours de maintenance. délai de rétablissement établi au 22 décembre!'

if __name__ == '__main__':
    # Lancer directement start_frontend.py avec subprocess
    subprocess.Popen(["python3", "Python/QT/Kicekifeqoa/Python/start_frontend.py"])

    # Si tu souhaites aussi démarrer le serveur Flask pour les interactions web
    app.run(host='0.0.0.0', port=5000)
