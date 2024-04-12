::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFDJ6eSCnCleeCbYJ5e31+/m7hUQJfPc9RKrVyaCPA+Ud/kD2SZ8jxW5blMcJHidUcRWkIAY3pg4=
::YAwzuBVtJxjWCl3EqQJhSA==
::ZR4luwNxJguZRRmh+lEkKXs=
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFDJ6eSCnCleeCbYJ5e31+/m7hUQJfPc9RKrVyaCPA+Ud/kD2SZ8jxW5blMcJHidxcAG/bwM4rHwMs3yAVw==
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
setlocal EnableDelayedExpansion

rem Définir le répertoire actuel
set "repertoire=%~dp0"

echo Fermer le logiciel si vous êtes en train d'effectuer une mise à jour...
echo -------
echo Une fois la fenêtre fermée, appuyez sur Entrée.&pause>nul

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
