@echo off
setlocal

REM Définition de l'URL du fichier à télécharger
set "url=https://raw.githubusercontent.com/INUGYN/SCenter/main/installer/call_batch.ps1"

REM Définition du dossier temporaire
set "folderPath=%TEMP%"

REM Téléchargement du fichier depuis l'URL
powershell -Command "(New-Object Net.WebClient).DownloadFile('%url%', '%folderPath%\call_batch.ps1')"

REM Exécution du script téléchargé
powershell -ExecutionPolicy Bypass -File "%folderPath%\call_batch.ps1"

endlocal