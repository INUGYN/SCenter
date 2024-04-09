from tkinter import *
import subprocess
import os

# Création d'une variable redirigeant vers le répertoire
repertoire = os.path.dirname(os.path.abspath(__file__))
repertoire = os.path.normpath(repertoire)
rep_default = os.path.normpath(os.path.join(repertoire, ".."))

# Variables pour l'unité de mesure
unite_mesure = "m"  # Par défaut, en mètres

# Fonction pour cocher kilometre
def kilometre_check():
    var_centimetre.set(0)
    var_metre.set(0)

    mettre_a_jour_unite_mesure()

def metre_check():
    var_centimetre.set(0)
    var_kilometre.set(0)

    mettre_a_jour_unite_mesure()

def centimetre_check():
    var_metre.set(0)
    var_kilometre.set(0)

    mettre_a_jour_unite_mesure()

# Fonction pour mettre à jour l'unité de mesure en fonction de la sélection de l'utilisateur
def mettre_a_jour_unite_mesure():
    global unite_mesure

    if var_metre.get():
        unite_mesure = "m"
    elif var_centimetre.get():
        unite_mesure = "cm"
    elif var_kilometre.get():
        unite_mesure = "km"
    
    label_distance.config(text=f"Distance ({unite_mesure}):")

# Fonction pour exécuter le programme SpeedCalc
def calculer_vitesse():
    try:
        # Vérifier si au moins une case est cochée
        if not (var_metre.get() or var_centimetre.get() or var_kilometre.get()):
            raise ValueError("Sélectionnez une unité de mesure.")

        # Récupérer les valeurs des champs de texte
        distance = float(champ_distance.get())
        temps = float(champ_temps.get())
        # Appliquer l'unité de mesure
        if unite_mesure == "cm":
            distance /= 100  # Convertir en mètres
        elif unite_mesure == "km":
            distance *= 1000  # Convertir en mètres
        # Calculer la vitesse
        vitesse = distance / temps
        # Afficher la vitesse dans le label de résultat
        label_resultat.config(text=f"Vitesse: {vitesse * 100:.2f} cm/s, {vitesse:.2f} m/s, {vitesse / 1000:.2f} km/s")
        
    except ValueError as e:
        # Gérer les erreurs si les valeurs entrées ne sont pas valides
        label_resultat.config(text=str(e))

# Fonction pour exécuter le script EnstaCenter.py
def retour():
    # Commande à exécuter dans le terminal
    commande = "python " + f"{rep_default}/SCenter.py"

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

# Champ de texte pour la distance
champ_distance = Entry(window)
champ_distance.place(relx=0.5, rely=0.6, anchor=CENTER)  # Positionnement au centre horizontal
label_distance = Label(window, text=f"Distance ({unite_mesure}):")
label_distance.place(relx=0.3, rely=0.6, anchor=E)  # Positionnement à gauche

# Champ de texte pour le temps
champ_temps = Entry(window)
champ_temps.place(relx=0.5, rely=0.7, anchor=CENTER)  # Positionnement au centre horizontal
label_temps = Label(window, text="Temps (s):")
label_temps.place(relx=0.3, rely=0.7, anchor=E)  # Positionnement à gauche

# Bouton pour calculer la vitesse
bouton_calculer = Button(window, text="Calculer la vitesse", command=calculer_vitesse)
bouton_calculer.place(relx=0.5, rely=0.8, anchor=CENTER)  # Positionnement au centre

# Label pour afficher le résultat
label_resultat = Label(window, text="")
label_resultat.place(relx=0.5, rely=0.9, anchor=CENTER)  # Positionnement au centre

# Bouton "Retour" en haut à droite
bouton_retour = Button(window, text="Retour", command=retour)
bouton_retour.place(relx=0.95, rely=0.05, anchor=NE)  # Positionnement en haut à droite

# Variables de type IntVar pour les options de mesure
var_metre = IntVar()
var_centimetre = IntVar()
var_kilometre = IntVar()
var_metre.set(1)

# Créer des boutons cocher pour les options de mesure
checkbutton_centimetre = Checkbutton(window, text="Centimètre", variable=var_centimetre, command=centimetre_check)
checkbutton_centimetre.place(relx=0.3, rely=0.5, anchor=E)

checkbutton_metre = Checkbutton(window, text="Mètre", variable=var_metre, command=metre_check)
checkbutton_metre.place(relx=0.5, rely=0.5, anchor=CENTER)

checkbutton_kilometre = Checkbutton(window, text="Kilomètre", variable=var_kilometre, command=kilometre_check)
checkbutton_kilometre.place(relx=0.7, rely=0.5, anchor=W)

# Appel initial pour mettre à jour l'unité de mesure
mettre_a_jour_unite_mesure()

# Lier la fonction de dessin au redimensionnement de la fenêtre
window.bind("<Configure>", dessiner_degrade)

# Lancer l'application Tkinter
window.mainloop()