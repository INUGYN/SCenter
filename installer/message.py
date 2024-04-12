import os
import plyer
import sys

# Obtient le chemin du répertoire du script Python
repertoire = os.path.dirname(os.path.abspath(__file__))

# Normalise le chemin pour obtenir des barres obliques
repertoire = os.path.normpath(repertoire)

def show_notification():
    plyer.notification.notify(
        title='Installation réussie !',
        message='SCenter à bien été installé.',
        app_icon=f'{repertoire}/logo.ico',  # Chemin vers une icône personnalisée si nécessaire
        timeout=5,  # Durée d'affichage de la notification en secondes
        ticker='Notification',  # Texte court qui apparaît brièvement sur certaines plateformes
        toast=True,  # Utiliser les notifications "toast" sur Windows 10
    )

# Appeler la fonction pour afficher la notification et jouer le son
show_notification()
sys.exit()
