@echo off
echo Se déplacer dans le répertoire 'docker'...
cd docker

echo Construction de l'image Docker pour le projet Kicekifeqoa...
docker build -t kicekifeqoa-image .

echo Lancement du conteneur Docker...
docker run -d -p 5000:5000 -v "%cd%":/workspace kicekifeqoa-image

echo Retour au répertoire parent...
cd ..

echo Le conteneur est lancé, accessible sur http://localhost:5000
pause
