from tkinter import *
import os
import subprocess

# Création d'une variable redirigeant vers le répertoire
repertoire = os.path.dirname(os.path.abspath(__file__))
repertoire = os.path.normpath(repertoire)
rep_default = os.path.normpath(os.path.join(repertoire, ".."))

# Fonction pour exécuter le script EnstaCenter.py
def retour():
    # Commande à exécuter dans le terminal
    commande = "python " + f'"{rep_default}/SCenter.py"'

    # Ouvrir un terminal et exécuter la commande
    subprocess.Popen(commande, shell=True)
    window.destroy()

unite_source = "s"
unite_cible = "s"

def ns_source_check():
    var_unite_us_source.set(0)
    var_unite_ms_source.set(0)
    var_unite_s_source.set(0)
    var_unite_min_source.set(0)
    var_unite_h_source.set(0)

    maj_unite_source()

def us_source_check():
    var_unite_ns_source.set(0)
    var_unite_ms_source.set(0)
    var_unite_s_source.set(0)
    var_unite_min_source.set(0)
    var_unite_h_source.set(0)

    maj_unite_source()

def ms_source_check():
    var_unite_ns_source.set(0)
    var_unite_us_source.set(0)
    var_unite_s_source.set(0)
    var_unite_min_source.set(0)
    var_unite_h_source.set(0)

    maj_unite_source()

def s_source_check():
    var_unite_ns_source.set(0)
    var_unite_us_source.set(0)
    var_unite_ms_source.set(0)
    var_unite_min_source.set(0)
    var_unite_h_source.set(0)

    maj_unite_source()

def min_source_check():
    var_unite_ns_source.set(0)
    var_unite_us_source.set(0)
    var_unite_ms_source.set(0)
    var_unite_s_source.set(0)
    var_unite_h_source.set(0)

    maj_unite_source()

def h_source_check():
    var_unite_ns_source.set(0)
    var_unite_us_source.set(0)
    var_unite_ms_source.set(0)
    var_unite_s_source.set(0)
    var_unite_min_source.set(0)

    maj_unite_source()

def ns_cible_check():
    var_unite_us_cible.set(0)
    var_unite_ms_cible.set(0)
    var_unite_s_cible.set(0)
    var_unite_min_cible.set(0)
    var_unite_h_cible.set(0)

    maj_unite_cible()

def us_cible_check():
    var_unite_ns_cible.set(0)
    var_unite_ms_cible.set(0)
    var_unite_s_cible.set(0)
    var_unite_min_cible.set(0)
    var_unite_h_cible.set(0)

    maj_unite_cible()

def ms_cible_check():
    var_unite_ns_cible.set(0)
    var_unite_us_cible.set(0)
    var_unite_s_cible.set(0)
    var_unite_min_cible.set(0)
    var_unite_h_cible.set(0)

    maj_unite_cible()

def s_cible_check():
    var_unite_ns_cible.set(0)
    var_unite_us_cible.set(0)
    var_unite_ms_cible.set(0)
    var_unite_min_cible.set(0)
    var_unite_h_cible.set(0)

    maj_unite_cible()

def min_cible_check():
    var_unite_ns_cible.set(0)
    var_unite_us_cible.set(0)
    var_unite_ms_cible.set(0)
    var_unite_s_cible.set(0)
    var_unite_h_cible.set(0)

    maj_unite_cible()

def h_cible_check():
    var_unite_ns_cible.set(0)
    var_unite_us_cible.set(0)
    var_unite_ms_cible.set(0)
    var_unite_s_cible.set(0)
    var_unite_min_cible.set(0)

    maj_unite_cible()


def dessiner_degrade(event=None):
    largeur = window.winfo_width()
    hauteur = window.winfo_height()
    canvas.delete("all")
    for i in range(hauteur):
        r = int(119 - (119 * i / hauteur))
        g = int(181 - (61 * i / hauteur))
        b = 254
        couleur = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        canvas.create_line(0, i, largeur, i, fill=couleur)

def convertir_temps(temps, unite_source, unite_cible):
    facteurs = {"ns": 1e9, "us": 1e6, "ms": 1e3, "s": 1, "min": 1/60, "h": 1/3600}
    temps_en_secondes = temps * facteurs[unite_cible]
    temps_converti = temps_en_secondes / facteurs[unite_source]
    return temps_converti

window = Tk()
window.title("Convertisseur de temps")
largeur_fenetre = 400
hauteur_fenetre = 350
window.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - largeur_fenetre) // 2
y_position = (screen_height - hauteur_fenetre) // 2
window.geometry(f"+{x_position}+{y_position}")
window.resizable(width=False, height=False)
window.attributes('-fullscreen', False)
window.iconbitmap(f"{rep_default}/logo.ico")
logo_image = PhotoImage(file=f"{rep_default}/logo.png").subsample(2)
canvas = Canvas(window)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
dessiner_degrade()
logo_label = Label(window, image=logo_image)
logo_label.place(relx=0.5, rely=0.2, anchor=CENTER)
champ_temps = Entry(window)
champ_temps.place(relx=0.5, rely=0.5, anchor=CENTER)
label_temps = Label(window, text=f"Temps({unite_source}):")
label_temps.place(relx=0.3, rely=0.5, anchor=E)
label_unite_source = Label(window, text="Unité de temps source:")
label_unite_source.place(relx=0.32, rely=0.42, anchor=E)
label_unite_cible = Label(window, text="Unité de temps cible:")
label_unite_cible.place(relx=0.3, rely=0.6, anchor=E)

var_unite_ns_source = IntVar()
var_unite_us_source = IntVar()
var_unite_ms_source = IntVar()
var_unite_s_source = IntVar()
var_unite_min_source = IntVar()
var_unite_h_source = IntVar()
var_unite_s_source.set(1)
checkbutton_ns_source = Checkbutton(window, text="ns", variable=var_unite_ns_source, command=ns_source_check)
checkbutton_ns_source.place(relx=0.38, rely=0.42, anchor=CENTER)
checkbutton_us_source = Checkbutton(window, text="µs", variable=var_unite_us_source, command=us_source_check)
checkbutton_us_source.place(relx=0.48, rely=0.42, anchor=CENTER)
checkbutton_ms_source = Checkbutton(window, text="ms", variable=var_unite_ms_source, command=ms_source_check)
checkbutton_ms_source.place(relx=0.58, rely=0.42, anchor=CENTER)
checkbutton_s_source = Checkbutton(window, text="s", variable=var_unite_s_source, command=s_source_check)
checkbutton_s_source.place(relx=0.676, rely=0.42, anchor=CENTER)
checkbutton_min_source = Checkbutton(window, text="min", variable=var_unite_min_source, command=min_source_check)
checkbutton_min_source.place(relx=0.776, rely=0.42, anchor=CENTER)
checkbutton_h_source = Checkbutton(window, text="h", variable=var_unite_h_source, command=h_source_check)
checkbutton_h_source.place(relx=0.876, rely=0.42, anchor=CENTER)

var_unite_ns_cible = IntVar()
var_unite_us_cible = IntVar()
var_unite_ms_cible = IntVar()
var_unite_s_cible = IntVar()
var_unite_min_cible = IntVar()
var_unite_h_cible = IntVar()
var_unite_s_cible.set(1)
checkbutton_ns_cible = Checkbutton(window, text="ns", variable=var_unite_ns_cible, command=ns_cible_check)
checkbutton_ns_cible.place(relx=0.38, rely=0.6, anchor=CENTER)
checkbutton_us_cible = Checkbutton(window, text="µs", variable=var_unite_us_cible, command=us_cible_check)
checkbutton_us_cible.place(relx=0.48, rely=0.6, anchor=CENTER)
checkbutton_ms_cible = Checkbutton(window, text="ms", variable=var_unite_ms_cible, command=ms_cible_check)
checkbutton_ms_cible.place(relx=0.58, rely=0.6, anchor=CENTER)
checkbutton_s_cible = Checkbutton(window, text="s", variable=var_unite_s_cible, command=s_cible_check)
checkbutton_s_cible.place(relx=0.676, rely=0.6, anchor=CENTER)
checkbutton_min_cible = Checkbutton(window, text="min", variable=var_unite_min_cible, command=min_cible_check)
checkbutton_min_cible.place(relx=0.776, rely=0.6, anchor=CENTER)
checkbutton_h_cible = Checkbutton(window, text="h", variable=var_unite_h_cible, command=h_cible_check)
checkbutton_h_cible.place(relx=0.876, rely=0.6, anchor=CENTER)

bouton_convertir = Button(window, text=f"Convertir en {unite_cible}", command=lambda: convertir_temps_click())
bouton_convertir.place(relx=0.5, rely=0.7, anchor=CENTER)
label_resultat = Label(window, text="")
label_resultat.place(relx=0.5, rely=0.8, anchor=CENTER)
bouton_retour = Button(window, text="Retour", command=retour)
bouton_retour.place(relx=0.95, rely=0.05, anchor=NE)
window.bind("<Configure>", dessiner_degrade)

def maj_unite_source():
    global unite_source

    if var_unite_ns_source.get():
        unite_source = "ns"
    elif var_unite_us_source.get():
        unite_source = "us"
    elif var_unite_ms_source.get():
        unite_source = "ms"
    elif var_unite_s_source.get():
        unite_source = "s"
    elif var_unite_min_source.get():
        unite_source = "min"
    elif var_unite_h_source.get():
        unite_source = "h"
    label_temps.config(text=f"Temps({unite_source}):")

def maj_unite_cible():
    global unite_cible

    if var_unite_ns_cible.get():
        unite_cible = "ns"
    elif var_unite_us_cible.get():
        unite_cible = "us"
    elif var_unite_ms_cible.get():
        unite_cible = "ms"
    elif var_unite_s_cible.get():
        unite_cible = "s"
    elif var_unite_min_cible.get():
        unite_cible = "min"
    elif var_unite_h_cible.get():
        unite_cible = "h"

    bouton_convertir.config(text=f"Convertir en {unite_cible}")

def convertir_temps_click():
    try:
        temps = float(champ_temps.get())
        maj_unite_source()
        maj_unite_cible()
        resultat = convertir_temps(temps, unite_source, unite_cible)
        # Mise à jour de l'unité de temps dans le texte du résultat
        label_resultat.config(text=f"Temps converti: {resultat} {unite_cible}")
    except ValueError:
        label_resultat.config(text="Valeur de temps invalide")


window.mainloop()
