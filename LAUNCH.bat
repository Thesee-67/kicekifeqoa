@echo off

REM Définir le chemin d'installation d'Anaconda basé sur l'utilisateur actuel
set CONDA_PATH=%USERPROFILE%\Anaconda3

REM Vérifier si Anaconda est installé
if not exist "%CONDA_PATH%\Scripts\activate.bat" (
    echo Anaconda n'est pas installé ou le chemin est incorrect.
    pause
    exit /b
)

REM Ajouter le chemin d'Anaconda aux variables d'environnement pour ce script
set PATH=%CONDA_PATH%\Scripts;%CONDA_PATH%\Library\bin;%PATH%

REM Créer l'environnement depuis le fichier environment.yml
conda env create --file=environment.yml

REM Activer l'environnement nouvellement créé
call "%CONDA_PATH%\Scripts\activate.bat" kicekifeqoa

REM Lancer le script Python main.py
python main.py

