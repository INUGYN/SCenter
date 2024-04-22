from tkinter import *
import subprocess
import os

# Création d'une variable redirigeant vers le répertoire
repertoire = os.path.dirname(os.path.abspath(__file__))
repertoire = os.path.normpath(repertoire)
rep_default = os.path.normpath(os.path.join(repertoire, ".."))

# Fonction pour exécuter le programme SpeedCalc
def calculer_mousse():
    try:
        # Récupérer les valeurs des champs de texte
        poids = float(champ_poids.get())
        volume = float(champ_volume.get())
        # Calculer la densité
        densite = poids / volume
        # Calculer le pourcentage d'air
        pourcentage_air = (1 - densite / densite_sans_air) * 100
        # Afficher les résultats
        label_resultat.config(text=f"Densité de la mousse: {densite:.2f} g/cm³\nPourcentage d'air: {pourcentage_air:.2f}%")
    except ValueError:
        # Gérer les erreurs si les valeurs entrées ne sont pas valides
        label_resultat.config(text="Entrez des valeurs numériques valides!")

# Fonction pour exécuter le script SCenter.py
def retour():
    # Commande à exécuter dans le terminal
    commande = "python " + f'"{rep_default}/SCenter.py"'

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
window.title("SCenter - FoamCalc")

# Taille de la fenêtre au démarrage
largeur_fenetre = 400
hauteur_fenetre = 450
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
window.iconbitmap(f"{rep_default}/logo.ico")

# Charger une image plus petite pour le logo
logo_image = PhotoImage(file=f"{rep_default}/logo.png").subsample(2)  # Réduire la taille de moitié

# Créer un canevas pour l'arrière-plan avec un dégradé
canvas = Canvas(window)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)  # Remplir tout l'espace disponible

# Dessiner le dégradé initial
dessiner_degrade()

# Créer un label pour afficher le logo
logo_label = Label(window, image=logo_image)
logo_label.place(relx=0.15, rely=0.2, anchor=CENTER)  # Positionnement au centre

# Champ pour calcul de masse d'air dans la mousse
Label(window, text="Poids de la mousse (g):").place(relx=0.15, rely=0.5, anchor=CENTER)
champ_poids = Entry(window)
champ_poids.place(relx=0.55, rely=0.5, anchor=CENTER)

Label(window, text="Volume de la mousse (cm³):").place(relx=0.15, rely=0.55, anchor=CENTER)
champ_volume = Entry(window)
champ_volume.place(relx=0.55, rely=0.55, anchor=CENTER)

# Densité de l'objet solide sans les pores d'air
densite_sans_air = 1.2  # Par exemple, pour le polyuréthane

# Bouton pour calculer la densité
bouton_calculer = Button(window, text="Calculer la densité", command=calculer_mousse)
bouton_calculer.place(relx=0.5, rely=0.6, anchor=CENTER)

# Label pour afficher le résultat
label_resultat = Label(window, text="")
label_resultat.place(relx=0.5, rely=0.75, anchor=CENTER)

# Bouton "Retour" en haut à droite
bouton_retour = Button(window, text="Retour", command=retour)
bouton_retour.place(relx=0.95, rely=0.05, anchor=NE)  # Positionnement en haut à droite

# Lier la fonction de dessin au redimensionnement de la fenêtre
window.bind("<Configure>", dessiner_degrade)

# Lancer l'application Tkinter
window.mainloop()
