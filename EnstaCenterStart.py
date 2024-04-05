from tkinter import *
from PIL import Image, ImageTk

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

# Créer un canevas pour l'arrière-plan avec un dégradé
canvas = Canvas(window)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)  # Remplir tout l'espace disponible

# Dessiner le dégradé initial
dessiner_degrade()

# Charger une image pour le logo
image = Image.open("loading.gif")
# Redimensionner l'image pour qu'elle rentre entièrement dans la fenêtre
image = image.resize((int(largeur_fenetre * 0.8), int(hauteur_fenetre * 0.8)), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(image)

# Créer un label pour afficher le logo centré
logo_label = Label(window, image=logo_image)
logo_label.place(relx=0.5, rely=0.5, anchor=CENTER)  # Positionnement au centre

# Lier la fonction de dessin au redimensionnement de la fenêtre
window.bind("<Configure>", dessiner_degrade)

# Lancer l'application Tkinter
window.mainloop()
