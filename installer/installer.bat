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
