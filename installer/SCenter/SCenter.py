from tkinter import *
import tkinter as tk
import subprocess
import webbrowser
import requests
import os


# Version actuellement installée
version_installee = "1.0"  # Remplacez par la version installée sur votre système

def patch():
    url_patch = "https://github.com/INUGYN/EnstaCenterMAJ/releases"
    webbrowser.open(url_patch)

def report_bug():
    url_report = "mailto:matteovalleix83@gmail.com?Subject=Bug%20Report%20from%20EnstaCenter"
    webbrowser.open(url_report)

# Création d'une variable redirigeant vers le répertoire
repertoire = os.path.dirname(os.path.abspath(__file__))
repertoire = os.path.normpath(repertoire)
rep_default = os.path.normpath(os.path.join(repertoire, ".."))
rep_default2 = os.path.normpath(os.path.join(rep_default, ".."))
print(rep_default)
rep_app = f"{rep_default2}/SCenter/AppFiles"
maj_activate = "non"


def maj_test():
    global maj_activate
    # URL de votre référentiel GitHub
    github_repo_api = 'https://api.github.com/repos/INUGYN/EnstaCenterMAJ'

    try:
        # Obtenir les informations des releases du référentiel
        releases_api = f"{github_repo_api}/releases"
        response = requests.get(releases_api)

        if response.status_code == 200:
            releases = response.json()
            if releases:
                latest_release = releases[0]
                latest_version = latest_release['tag_name']
                latest_version_url = latest_release['html_url']

                if latest_version != version_installee:
                    maj(latest_version)
                else:
                    print("Votre version est à jour.")
            else:
                print("Aucune release disponible pour ce référentiel.")
        else:
            print("Erreur lors de la récupération des informations des releases (Code de statut :", response.status_code, ")")
    except Exception as e:
        print("Pas d'internet:", e)


def maj(latest_version):
    # Fonction appelée lorsque le bouton de mise à jour est cliqué
    def update_button_click():
        webbrowser.open("https://github.com/INUGYN/EnstaCenter/archive/refs/heads/main.zip")
        global maj_activate
        maj_activate = "oui"
        exit()

    # Fonction appelée lorsque le bouton Ignorer est cliqué
    def ignore_button_click():
        window.destroy()

    # Création de la fenêtre
    window = tk.Tk()
    window.title("Mise à jour")
    window.iconbitmap("logo.ico")

    # Obtention des dimensions de l'écran
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Dimensions de la fenêtre
    window_width = 400
    window_height = 250

    # Calcul des coordonnées pour centrer la fenêtre
    x = int(screen_width / 2 - window_width / 2)
    y = int(screen_height / 2 - window_height / 2)

    # Positionnement de la fenêtre au centre de l'écran
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Texte indiquant qu'il y a une mise à jour
    text_label = tk.Label(window, text=f"La version v{latest_version} est disponible !", font=("Arial", 14))
    text_label.pack(pady=20)

    text_label2 = tk.Label(window, text=f"Vous avez la version v{version_installee}.", font=("Arial", 14))
    text_label2.pack(pady=20)

    # Bouton de mise à jour
    update_button = tk.Button(window, text="Mettre à jour", font=("Arial", 12), command=update_button_click)
    update_button.pack(pady=10)

    # Bouton Ignorer
    ignore_button = tk.Button(window, text="Ignorer", font=("Arial", 12), command=ignore_button_click)
    ignore_button.pack(pady=10)

    # Boucle principale de la fenêtre
    window.mainloop()


# Fonction pour exécuter le programme SpeedCalc
def lancer_speedcalc():
    # Commande à exécuter dans le terminal
    commande = f"python {rep_app}/speedcalc.py"

    # Ouvrir un terminal et exécuter la commande
    subprocess.Popen(commande, shell=True)
    window.destroy()


# Fonction pour exécuter le programme FoamCalc
def lancer_foamcalc():
    # Commande à exécuter dans le terminal
    commande = f"python {rep_app}/FoamCalc.py"

    # Ouvrir un terminal et exécuter la commande
    subprocess.Popen(commande, shell=True)
    window.destroy()

# Fonction pour exécuter le programme FoamCalc
def lancer_timeconverter():
    # Commande à exécuter dans le terminal
    commande = f"python {rep_app}/TimeConverter.py"

    # Ouvrir un terminal et exécuter la commande
    subprocess.Popen(commande, shell=True)
    window.destroy()

# Fonction pour exécuter le programme Clock
def lancer_clock():
    # Commande à exécuter dans le terminal
    commande = f"python {rep_app}/clock.py"

    # Ouvrir un terminal et exécuter la commande
    subprocess.Popen(commande, shell=True)
    window.destroy()



# Fonction pour dessiner le dégradé
def dessiner_degrade(event=None):
    # Taille du canevas
    largeur = window.winfo_width()
    hauteur = window.winfo_height()
    # Effacer tout contenu précédent
    canvas.delete("all")
    # Dessiner un dégradé diagonal allant de #77B5FE à #0080FF
    for i in range(hauteur):
        r = int(119 - (119 * i / hauteur))  # Diminuer progressivement la composante rouge
        g = int(181 - (61 * i / hauteur))  # Diminuer progressivement la composante verte
        b = 254  # Bleu constant
        couleur = '#{:02x}{:02x}{:02x}'.format(r, g, b)  # Format de couleur hexadécimal
        canvas.create_line(0, i, largeur, i, fill=couleur)


# Créer la fenêtre principale
window = Tk()

# Nom de la fenêtre
window.title("EnstaCenter")

# Taille de la fenêtre au démarrage
largeur_fenetre = 400
hauteur_fenetre = 350
window.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")

# Centrer la fenêtre à l'écran
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - largeur_fenetre) // 2
y_position = (screen_height - hauteur_fenetre) // 2
window.geometry(f"+{x_position}+{y_position}")

# Empêcher le redimensionnement de la fenêtre
window.resizable(width=False, height=False)

# Empêcher la mise en plein écran
window.attributes('-fullscreen', False)

# Charger l'icône
window.iconbitmap(f"{repertoire}/logo.ico")

# Charger une image plus petite pour le logo
logo_image = PhotoImage(file=f"{repertoire}/logo.png").subsample(2)  # Réduire la taille de moitié

# Créer un canevas pour l'arrière-plan avec un dégradé
canvas = Canvas(window)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)  # Remplir tout l'espace disponible

# Dessiner le dégradé initial
dessiner_degrade()

# Afficher la version
version_text = Label(window, text=f"Version : {version_installee}")
# Positionner le Text dans la fenêtre
version_text.place(relx=0.0, rely=0.0)

# Bouton "PatchNote" en haut à droite
bouton_patchnote = Button(window, text="Patch Note", command=patch)
bouton_patchnote.place(relx=0.95, rely=0.05, anchor=NE)  # Positionnement en haut à droite

# Bouton "Report Bug" en haut à droite
bouton_report = Button(window, text="Report Bug", command=report_bug)
bouton_report.place(relx=0.95, rely=0.15, anchor=NE)


# Créer un label pour afficher le logo
logo_label = Label(window, image=logo_image)
logo_label.place(relx=0.5, rely=0.2, anchor=CENTER)  # Positionnement au centre

# Bouton pour lancer SpeedCalc
bouton_speedcalc = Button(window, text="SpeedCalc", command=lancer_speedcalc, width=15)
bouton_speedcalc.place(relx=0.2, rely=0.7, anchor=CENTER)  # Positionnement au centre

# Bouton pour lancer SpeedCalc
bouton_speedcalc = Button(window, text="Time Converter", command=lancer_timeconverter, width=15)
bouton_speedcalc.place(relx=0.2, rely=0.8, anchor=CENTER)  # Positionnement au centre

# Bouton placeholder
bouton_placeholder = Button(window, text="FoamCalc", command=lancer_foamcalc, width=15)
bouton_placeholder.place(relx=0.2, rely=0.9, anchor=CENTER)  # Positionnement au centre

# Bouton placeholder
bouton_placeholder = Button(window, text="Clock", command=lancer_clock, width=15)
bouton_placeholder.place(relx=0.5, rely=0.7, anchor=CENTER)  # Positionnement au centre

# Bouton placeholder
bouton_placeholder = Button(window, text="SOON", command="", width=15)
bouton_placeholder.place(relx=0.5, rely=0.8, anchor=CENTER)  # Positionnement au centre

# Bouton placeholder
bouton_placeholder = Button(window, text="SOON", command="", width=15)
bouton_placeholder.place(relx=0.5, rely=0.9, anchor=CENTER)  # Positionnement au centre

# Bouton placeholder
bouton_placeholder = Button(window, text="SOON", command="", width=15)
bouton_placeholder.place(relx=0.8, rely=0.7, anchor=CENTER)  # Positionnement au centre

# Bouton placeholder
bouton_placeholder = Button(window, text="SOON", command="", width=15)
bouton_placeholder.place(relx=0.8, rely=0.8, anchor=CENTER)  # Positionnement au centre

# Bouton placeholder
bouton_placeholder = Button(window, text="SOON", command="", width=15)
bouton_placeholder.place(relx=0.8, rely=0.9, anchor=CENTER)  # Positionnement au centre

# Lier la fonction de dessin au redimensionnement de la fenêtre
window.bind("<Configure>", dessiner_degrade)

# Appeler la fonction de test de mise à jour
maj_test()

# Lancer l'application Tkinter
window.mainloop()
