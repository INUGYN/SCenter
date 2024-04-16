::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFDJ6eSCnCleeCbYJ5e31+/m7hUQJfPc9RLz437qaJfIv40v3YZch2n9IpMcDCxQWdxGkDg==
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
::Zh4grVQjdCyDJGyX8VAjFDJ6eSCnCleeCbYJ5e31+/m7hUQJfPc9RLz437qaJfIv40v3YZch2n9IpOICHw9Zch6ufEExsWsi
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
setlocal

REM Définition du chemin du bureau de l'utilisateur
set "desktopPath=%USERPROFILE%\Desktop"

REM Définition de l'URL du référentiel à télécharger (en utilisant l'archive ZIP du référentiel)
set "url=https://github.com/INUGYN/SCenter/archive/main.zip"

REM Définition du chemin du fichier ZIP à télécharger
set "zipFilePath=%desktopPath%\SCenter.zip"

REM Téléchargement de l'archive du référentiel depuis l'URL directement sur le bureau
powershell -Command "(New-Object Net.WebClient).DownloadFile('%url%', '%zipFilePath%')"

REM Extrait l'archive directement sur le bureau
powershell Expand-Archive -Path '%zipFilePath%' -DestinationPath '%desktopPath%'

REM Déplacement vers le dossier installer
cd /d "%desktopPath%\SCenter-main\installer"

REM Exécution du script call_batch.ps1
powershell -ExecutionPolicy Bypass -File "%desktopPath%\SCenter-main\installer\call_batch.ps1"

endlocal
