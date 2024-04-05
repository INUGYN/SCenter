from tkinter import *
import subprocess
import os

# Fonction pour exécuter le programme SpeedCalc
def calculer_vitesse():
    try:
        # Récupérer les valeurs des champs de texte
        distance = float(champ_distance.get())
        temps = float(champ_temps.get())
        # Calculer la vitesse
        vitesse = distance / temps
        # Afficher la vitesse dans le label de résultat
        label_resultat.config(text=f"Vitesse: {vitesse:.2f} m/s")
    except ValueError:
        # Gérer les erreurs si les valeurs entrées ne sont pas valides
        label_resultat.config(text="Entrez des valeurs numériques valides!")

# Fonction pour exécuter le script EnstaCenter.py
def retour():
    # Récupérer le chemin complet du répertoire actuel
    chemin_actuel = os.path.dirname(os.path.abspath(__file__))
    # Spécifier le chemin complet vers EnstaCenter.py
    chemin_enstacenter = os.path.join(chemin_actuel, "EnstaCenter.py")
    # Commande à exécuter dans le terminal
    commande = "python " + chemin_enstacenter

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
window.iconbitmap("logo.ico")

# Charger une image plus petite pour le logo
logo_image = PhotoImage(file="logo.png").subsample(2)  # Réduire la taille de moitié

# Créer un canevas pour l'arrière-plan avec un dégradé
canvas = Canvas(window)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)  # Remplir tout l'espace disponible

# Dessiner le dégradé initial
dessiner_degrade()

# Créer un label pour afficher le logo
logo_label = Label(window, image=logo_image)
logo_label.place(relx=0.5, rely=0.2, anchor=CENTER)  # Positionnement au centre

# Champ de texte pour la distance
champ_distance = Entry(window)
champ_distance.place(relx=0.5, rely=0.5, anchor=CENTER)  # Positionnement au centre horizontal
label_distance = Label(window, text="Distance (m):")
label_distance.place(relx=0.3, rely=0.5, anchor=E)  # Positionnement à gauche

# Champ de texte pour le temps
champ_temps = Entry(window)
champ_temps.place(relx=0.5, rely=0.6, anchor=CENTER)  # Positionnement au centre horizontal
label_temps = Label(window, text="Temps (s):")
label_temps.place(relx=0.3, rely=0.6, anchor=E)  # Positionnement à gauche

# Bouton pour calculer la vitesse
bouton_calculer = Button(window, text="Calculer la vitesse", command=calculer_vitesse)
bouton_calculer.place(relx=0.5, rely=0.7, anchor=CENTER)  # Positionnement au centre

# Label pour afficher le résultat
label_resultat = Label(window, text="")
label_resultat.place(relx=0.5, rely=0.8, anchor=CENTER)  # Positionnement au centre

# Bouton "Retour" en haut à droite
bouton_retour = Button(window, text="Retour", command=retour)
bouton_retour.place(relx=0.95, rely=0.05, anchor=NE)  # Positionnement en haut à droite

# Lier la fonction de dessin au redimensionnement de la fenêtre
window.bind("<Configure>", dessiner_degrade)

# Lancer l'application Tkinter
window.mainloop()
