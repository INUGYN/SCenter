Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Obtenir le chemin du répertoire du script PowerShell
$scriptDirectory = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Création de la fenêtre principale
$form = New-Object System.Windows.Forms.Form
$form.Text = "SCenter - Installation"
$form.Size = New-Object System.Drawing.Size(600,400) # Taille modifiée

# Charger l'icône depuis le fichier logo.ico dans le répertoire du script
$iconFilePath = Join-Path -Path $scriptDirectory -ChildPath "logo.ico"
if (Test-Path $iconFilePath) {
    $icon = New-Object System.Drawing.Icon($iconFilePath)
    $form.Icon = $icon
} else {
    Write-Host "Erreur: Fichier logo.ico introuvable dans le répertoire du script."
    exit
}

$form.StartPosition = "CenterScreen"

# Création du cadre de terminal
$terminalFrame = New-Object System.Windows.Forms.RichTextBox
$terminalFrame.Location = New-Object System.Drawing.Point(10, 10)
$terminalFrame.Size = New-Object System.Drawing.Size(560, 230) # Taille modifiée
$terminalFrame.Font = New-Object System.Drawing.Font("Consolas",10)
$terminalFrame.ScrollBars = "Vertical"
$terminalFrame.BackColor = [System.Drawing.Color]::White
$terminalFrame.ReadOnly = $true
$terminalFrame.Add_Enter({
    $form.Focus()
})
$form.Controls.Add($terminalFrame)

# Fonction pour afficher des messages dans le terminal
function WriteToTerminal([string]$message) {
    # Ajouter le message
    $terminalFrame.AppendText("$message`n")
    
    # Faire défiler automatiquement vers le bas
    $terminalFrame.SelectionStart = $terminalFrame.Text.Length
    $terminalFrame.ScrollToCaret()
}

# Construire le chemin complet vers le fichier batch
$batchFilePath = Join-Path -Path $scriptDirectory -ChildPath "make_exe.bat"

# Case à cocher pour l'acceptation des conditions d'utilisation
$acceptCheckbox = New-Object System.Windows.Forms.CheckBox
$acceptCheckbox.Location = New-Object System.Drawing.Point(10, 250)
$acceptCheckbox.Size = New-Object System.Drawing.Size(400, 20) # Taille modifiée
$acceptCheckbox.Text = "J'accepte les conditions d'utilisation"
$form.Controls.Add($acceptCheckbox)

# Bouton d'installation avec le chemin du fichier batch construit automatiquement
$installButton = New-Object System.Windows.Forms.Button
$installButton.Location = New-Object System.Drawing.Point(50, 300) # Position modifiée
$installButton.Size = New-Object System.Drawing.Size(120, 30)
$installButton.Text = "Installer"
$installButton.Enabled = $false
$installButton.Add_Click({
    if (-not $acceptCheckbox.Checked) {
        WriteToTerminal "Veuillez accepter les conditions d'utilisation."
        return
    }
    
    WriteToTerminal "Installation en cours..."
    
    try {
        # Configuration des informations de démarrage du processus pour exécution en tant qu'administrateur
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = "cmd.exe"
        $psi.Arguments = "/c `"$batchFilePath`""
        $psi.Verb = "runas"  # Exécution en tant qu'administrateur
        $psi.RedirectStandardOutput = $true
        $psi.UseShellExecute = $false
        $psi.CreateNoWindow = $true
        
        # Démarrage du processus
        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $psi

        # Démarrage du processus
        $process.Start() | Out-Null

        # Lecture de la sortie du processus ligne par ligne
        while (!$process.HasExited) {
            $output = $process.StandardOutput.ReadLine()
            if ($output -ne $null) {
                WriteToTerminal $output
            }
        }

        # Lecture et affichage de la sortie restante
        $remainingOutput = $process.StandardOutput.ReadToEnd()
        if ($remainingOutput -ne $null) {
            WriteToTerminal $remainingOutput
        }

        if ($process.ExitCode -eq 0) {
            WriteToTerminal "Installation terminée."
            
            # Supprimer le fichier SCenter.zip du bureau s'il existe
            $desktopPath = [Environment]::GetFolderPath("Desktop")
            $scenterZipFile = Join-Path -Path $desktopPath -ChildPath "SCenter.zip"
            if (Test-Path $scenterZipFile) {
                Remove-Item $scenterZipFile -Force
                WriteToTerminal "Fichier SCenter.zip supprimé."
            }

            # Fermer automatiquement la fenêtre après 3 secondes
            Start-Sleep -Seconds 3
            $form.Close()
        } else {
            WriteToTerminal "Erreur lors de l'installation."
        }
    } catch {
        WriteToTerminal "Erreur lors de l'installation : $_"
    }
})
$form.Controls.Add($installButton)

# Ajouter un gestionnaire d'événements pour surveiller les changements de la case à cocher
$acceptCheckbox.Add_CheckedChanged({
    if ($acceptCheckbox.Checked) {
        $installButton.Enabled = $true
    } else {
        $installButton.Enabled = $false
    }
})

# Bouton pour quitter
$quitButton = New-Object System.Windows.Forms.Button
$quitButton.Location = New-Object System.Drawing.Point(450, 300) # Position modifiée
$quitButton.Size = New-Object System.Drawing.Size(120, 30)
$quitButton.Text = "Quitter"
$quitButton.Add_Click({
    $form.Close()
})
$form.Controls.Add($quitButton)

# Afficher la fenêtre
$form.ShowDialog() | Out-Null
