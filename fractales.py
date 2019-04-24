# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:16:42 2019

Quelques exemples d'utilisation du canevas dans une fenêtre graphique gérée par
le module tkinter.

@author: Cédric Berteletti
"""



CANVAS_WIDTH=900
CANVAS_HEIGHT=600



## IMPORTATION DES PACKAGES UTILES

from tkinter import Tk, Canvas, TOP, Button
from math import cos, sin, pi
import random



## DECLARATION DE FONCTIONS

def circle(canvas, x, y, r, couleur="black"):
    "Tracé d'un cercle de centre (x,y) et de rayon r"
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=couleur)



def branches(canvas, x1, y1, x2, y2, nombres_branches=3, echelles_branches=[0.5, 0.8, 0.5],
             orientations_branches=[45, 10, -45], couleur="black", recursions=5):
    "Fonction récursive permettant de tracer la ligne (x1, y1)-(x2, y2) et de la \
    prolonger par `nombres_branches` lignes avec différentes échelles et orientations"

    # Tracer la branche actuelle
    canvas.create_line(x1, y1, x2, y2, fill=couleur)

    if recursions > 0:
        # Si on n'a pas atteint les feuilles de l'arbre (recursions == 0)
        # Calculer les sous-branches
        for i in range(nombres_branches):
            # Création de la sous-branche i identique à la branche principale
            # placée à l'origine du repère
            tempx1 = 0
            tempy1 = 0
            tempx2 = x2-x1
            tempy2 = y2-y1

            # Mise à l'échelle de la sous-branche
            tempx2 = tempx2 * echelles_branches[i]
            tempy2 = tempy2 * echelles_branches[i]

            # Rotation de la sous-branche
            angle = orientations_branches[i] * 2.0 * pi / 360.0 # conversion degrés -> radian
            tempx3 = tempx2 * cos(angle) + tempy2 * sin(angle)
            tempy3 = - tempx2 * sin(angle) + tempy2 * cos(angle)

            # Translation de la sous-branche au bout de la branche principale
            tempx1 += x2
            tempy1 += y2
            tempx3 += x2
            tempy3 += y2

            # Appel récursif pour tracer la sous-branche et les éventuelles sous-sous-branches
            branches(canvas, tempx1, tempy1, tempx3, tempy3, nombres_branches, echelles_branches,
                     orientations_branches, couleur, recursions-1)


def koch(canvas, x1, y1, x2, y2, couleur="black", recursions=5):
    "Fonction récursive pour créer la courbe de Koch à partir d'une ligne (x1, y1)-(x2, y2) \
    https://fr.wikipedia.org/wiki/Flocon_de_Koch"

    if recursions== 0:
        # Tracer la ligne actuelle
        canvas.create_line(x1, y1, x2, y2, fill=couleur)
    else:
        # Subdiviser la ligne (1-2) actuelle en 4 segments (1-3-5-4-2)

        # Lignes extrêmes
        dx = x2-x1
        dy = y2-y1
        x3 = x1 + dx / 3
        y3 = y1 + dy / 3
        x4 = x1 + 2 * dx / 3
        y4 = y1 + 2 * dy / 3
        koch(canvas, x1, y1, x3, y3, couleur, recursions-1)
        koch(canvas, x4, y4, x2, y2, couleur, recursions-1)

        # "Pointe"
        # Coordonnées du point 4 dans un repère ayant pour centre le point 3
        tempx = x4-x3
        tempy = y4-y3
        # Rotation de 60° de ce nouveau point (triangle isocèle)
        angle = 60 * 2.0 * pi / 360.0 # conversion degrés -> radian
        tempx2 = tempx * cos(angle) + tempy * sin(angle)
        tempy2 = - tempx * sin(angle) + tempy * cos(angle)
        # Coordonnées du point dans le repère initial et tracé
        tempx3 = tempx2 + x3
        tempy3 = tempy2 + y3
        koch(canvas, x3, y3, tempx3, tempy3, couleur, recursions-1)
        koch(canvas, tempx3, tempy3, x4, y4, couleur, recursions-1)


def sierpinski(canvas, x1, y1, x2, y2, x3, y3, couleur="black", recursions=5):
    "Fonction récursive permettant de tracer le triangle de Sierpiński \
    de sommets (x1, y1), (x2, y2) et (x3, y3) \
    https://fr.wikipedia.org/wiki/Triangle_de_Sierpi%C5%84ski"
    print("TODO")


def clear():
    canvas.delete("all")

def draw_random_fractale():
    f = random.randint(1, 3)

    if f == 1:
        x1 = random.randint(CANVAS_WIDTH / 4, 3 * CANVAS_WIDTH / 4)
        y1 = random.randint(CANVAS_HEIGHT / 4, 3 * CANVAS_HEIGHT / 4)
        x2 = random.randint(CANVAS_WIDTH / 4, 3 * CANVAS_WIDTH / 4)
        y2 = random.randint(CANVAS_HEIGHT / 4, 3 * CANVAS_HEIGHT / 4)
        branches(canvas, x1, y1, x2, y2)
    elif f == 2:
        print("TODO")

    elif f == 3:
        print("TODO")



## PROGRAMME PRINCIPAL

# Préparation de la fenêtre et du canevas de dessin
window = Tk()
canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack(side=TOP, padx=5, pady=5)

button_quit = Button(window, text="Quitter", command = window.destroy)
button_quit.pack(side="right")

button_clear = Button(window, text="Effacer", command = clear)
button_clear.pack(side="left")

button_draw = Button(window, text="Dessiner une fractale au hasard", command = draw_random_fractale)
button_draw.pack(side="bottom")

#cercle(canvas, 200, 200, 100)

# Fougère
branches(canvas, 600, 600, 600, 500, nombres_branches=3, echelles_branches=[0.3, 0.9, 0.3],
             orientations_branches=[30, -5, -25], couleur="green", recursions=10)

# Arbre
branches(canvas, 350, 350, 350, 250, nombres_branches=4, echelles_branches=[0.5, 0.6, 0.7, 0.8],
             orientations_branches=[25, 5, -20, -35], couleur="green", recursions=5)
# Racines
branches(canvas, 350, 350, 350, 400, nombres_branches=3, echelles_branches=[0.7, 0.9, 0.8],
             orientations_branches=[-45, -10, 45], couleur="brown", recursions=4)

# Flocon de Koch
koch(canvas, 20, 100, 220, 100)
koch(canvas, 220, 100, 120, 273)
koch(canvas, 120, 273, 20, 100)

# "Puzzle" de Koch !
koch(canvas, 20, 400, 220, 400)
koch(canvas, 20, 400, 120, 487)
koch(canvas, 120, 487, 220, 400)

# Triangle de Sierpiński
#sierpinski (canvas, 700, 600, 800, 427, 900, 600)

# Affichage
window.mainloop()


