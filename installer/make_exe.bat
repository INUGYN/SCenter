@echo off
setlocal EnableDelayedExpansion

rem Définir le répertoire actuel
set "repertoire=%~dp0"


rem Vérification de l'installation de Python avec Chocolatey

rem Vérifier si Chocolatey est installé
choco --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Chocolatey n'est pas installé. Installation de Chocolatey...
    @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    if %errorlevel% neq 0 (
        echo L'installation de Chocolatey a échoué. Veuillez installer Chocolatey manuellement et réessayez.
        exit /b %errorlevel%
    )
    echo Chocolatey a été installé avec succès.
) else (
    echo Chocolatey est déjà installé.
)

rem Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installé. Installation de Python...
    choco install python311 -y
    if %errorlevel% neq 0 (
        echo L'installation de Python a échoué. Veuillez installer Python manuellement et réessayez.
        exit /b %errorlevel%
    ) else (
        echo Python a été installé avec succès.
    )
) else (
    echo Python est déjà installé.
)

pushd "%repertoire%"

rem Installer les dépendances Python
echo Installation des dépendances Python...
pip install -r requirements.txt
pip install --upgrade -r requirements.txt

popd

pushd "%repertoire%"

rem Compiler le code
echo Compilation du code...
python setup.py build

rem Exécuter le script message.py
python message.py

popd

echo Terminé.
