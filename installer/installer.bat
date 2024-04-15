@echo off
setlocal

REM Définition du chemin du bureau de l'utilisateur
set "desktopPath=%USERPROFILE%\Desktop"

REM Définition du chemin relatif vers le fichier contenant le token
set "tokenFile=token.txt"

REM Construction du chemin absolu vers le fichier
set "tokenFilePath=%~dp0%tokenFile%"

REM Vérification de l'existence du fichier de token
if not exist "%tokenFilePath%" (
    echo Le fichier de token n'existe pas.
    exit /b 1
)

REM Lecture du jeton à partir du fichier
set /p githubToken=<"%tokenFilePath%"

REM Vérification que le jeton est défini
if "%githubToken%"=="" (
    echo Le jeton d'accès GitHub n'est pas défini.
    exit /b 1
)

REM Définition de l'URL du référentiel à télécharger (en utilisant l'archive ZIP du référentiel)
set "username=INUGYN"
set "repository=SCenter"
set "url=https://github.com/%username%/%repository%/archive/main.zip?access_token=%githubToken%"

REM Affichage de l'URL pour vérification
echo L'URL générée est : %url%

REM Définition du chemin du fichier ZIP à télécharger
set "zipFilePath=%desktopPath%\SCenter.zip"

REM Téléchargement de l'archive du référentiel depuis l'URL directement sur le bureau
echo Téléchargement de l'archive depuis l'URL...
powershell -Command "(New-Object Net.WebClient).DownloadFile('%url%', '%zipFilePath%')"

REM Extrait l'archive directement sur le bureau
echo Extraction de l'archive...
powershell Expand-Archive -Path '%zipFilePath%' -DestinationPath '%desktopPath%'

REM Déplacement vers le dossier installer
cd /d "%desktopPath%\SCenter-main\installer"

REM Exécution du script call_batch.ps1
echo Exécution du script call_batch.ps1...
powershell -ExecutionPolicy Bypass -File "%desktopPath%\SCenter-main\installer\call_batch.ps1"

endlocal
