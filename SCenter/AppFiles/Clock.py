from tkinter import *
import subprocess
import os
from datetime import datetime, timedelta

# Création d'une variable redirigeant vers le répertoire
repertoire = os.path.dirname(os.path.abspath(__file__))
repertoire = os.path.normpath(repertoire)
rep_default = os.path.normpath(os.path.join(repertoire, ".."))

# Déclaration des variables globales
stopwatch_update_id = None
start_time = None
is_running = False

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

# Fonction pour mettre à jour l'horloge
def update_clock():
    # Obtenir l'heure actuelle
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")  # Format HH:MM:SS

    # Mettre à jour l'étiquette de l'horloge avec l'heure actuelle
    clock_label.config(text=current_time)

    # Planifier la prochaine mise à jour de l'horloge après 1 seconde (1000 millisecondes)
    window.after(1000, update_clock)

# Fonction pour mettre à jour le chronomètre
def update_stopwatch():
    # Utiliser des variables globales
    global start_time, stopwatch_update_id

    # Calculer le temps écoulé depuis le démarrage du chronomètre
    elapsed_time = datetime.now() - start_time

    # Formater le temps écoulé
    elapsed_time_str = str(elapsed_time).split(".")[0]  # Ignorer les microsecondes
    ms_str = f".{elapsed_time.microseconds // 1000:03}"  # Formatage des millisecondes

    # Mettre à jour l'étiquette du chronomètre avec le temps écoulé
    stopwatch_label.config(text=elapsed_time_str + ms_str)

    # Planifier la prochaine mise à jour du chronomètre après 100 millisecondes
    stopwatch_update_id = window.after(100, update_stopwatch)

# Fonction pour démarrer le chronomètre
def start_stopwatch():
    # Utiliser une variable globale
    global start_time, is_running

    if is_running == False:
        start_time = datetime.now()
        is_running = True
        update_stopwatch()

# Fonction pour arrêter le chronomètre
def stop_stopwatch():
    # Utiliser une variable globale
    global is_running

    if is_running:
        is_running = False
        window.after_cancel(stopwatch_update_id)  # Arrêter la mise à jour du chronomètre

# Fonction pour réinitialiser le chronomètre
def reset_stopwatch():
    global start_time, is_running
    is_running = False
    start_time = None
    stopwatch_label.config(text="0:00:00.000")
    window.after_cancel(stopwatch_update_id)  # Arrêter la mise à jour du chronomètre

# Fonction pour mettre en pause le chronomètre
def pause_stopwatch():
    try:
        # Utiliser des variables globales
        global is_running, start_time, pause_time

        if is_running == True:
            is_running = False
            pause_time = datetime.now()  # Enregistrer le moment où le chronomètre est mis en pause
            window.after_cancel(stopwatch_update_id)  # Arrêter la mise à jour du chronomètre
            pause_button.config(text="Reprendre")  # Changer le texte du bouton en "Reprendre"
        elif is_running == False:
            is_running = True
            if pause_time:  # Vérifier si le chronomètre a été mis en pause au moins une fois
                # Reprendre le temps à partir du moment où il a été mis en pause
                start_time += datetime.now() - pause_time
            else:
                start_time = datetime.now()  # Sinon, démarrer le chronomètre depuis le début
            update_stopwatch()  # Reprendre la mise à jour du chronomètre
            pause_button.config(text="Pause")  # Changer le texte du bouton en "Pause"
    except:
        return


# Créer la fenêtre principale
window = Tk()

# Nom de la fenêtre
window.title("SCenter - Clock")

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

# Créer une étiquette pour afficher l'horloge
clock_label = Label(window, font=("Helvetica", 24))
clock_label.place(relx=0.5, rely=0.35, anchor=CENTER)  # Positionnement au centre

# Créer une étiquette pour afficher le chronomètre
stopwatch_label = Label(window, text="0:00:00.000", font=("Helvetica", 24))
stopwatch_label.place(relx=0.5, rely=0.55, anchor=CENTER)  # Positionnement au centre

# Bouton "Démarrer" pour le chronomètre
start_button = Button(window, text="Démarrer", command=start_stopwatch)
start_button.place(relx=0.3, rely=0.9, anchor=CENTER)

# Bouton "Arrêter" pour le chronomètre
stop_button = Button(window, text="Arrêter", command=stop_stopwatch)
stop_button.place(relx=0.5, rely=0.9, anchor=CENTER)

# Bouton "Pause" pour le chronomètre
pause_button = Button(window, text="Pause", command=pause_stopwatch)
pause_button.place(relx=0.5, rely=0.8, anchor=CENTER)

# Bouton "Réinitialiser" pour le chronomètre
reset_button = Button(window, text="Réinitialiser", command=reset_stopwatch)
reset_button.place(relx=0.7, rely=0.9, anchor=CENTER)

# Lancer la fonction pour mettre à jour l'horloge
update_clock()

# Bouton "Retour" en haut à droite
bouton_retour = Button(window, text="Retour", command=retour)
bouton_retour.place(relx=0.95, rely=0.05, anchor=NE)  # Positionnement en haut à droite

# Lancer l'application Tkinter
window.mainloop()
