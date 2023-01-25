# module immeuble

from tkinter import OUTSIDE
from couleur_aleatoire import couleur_aleatoire
import random
from facade import facade
from rdc import rdc
from etage import etage
from toit import toit
import turtle

turtle.speed(100)    #augmentation de la vitesse de tortue

def immeuble(x, y_sol):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    Cette fonction dessine un immeuble Le nombre d'étage est compris aléatoirement entre 0 et 4
    La couleur de la façade et la couleur de la porte sont tirées au hasard
    '''
    

  
    couleur_de_facade = couleur_aleatoire()  #couleur aléatoire pour toutes les facades
    print(couleur_de_facade)

    
    rdc(x,y_sol,couleur_de_facade, couleur_aleatoire())  #création de la base de l'immeuble --> le rdc avec la couleur de facade et une autre couleur pour la porte

    
    niv=1
    for i in range(0,(random.randint(0,4))):                   #création de 0 à 4 étages 
        etage(x,y_sol+60+60*i,couleur_de_facade,1)            #coordonnées des étages + couleur
        niv+=1
    print(niv)
    toit(x+70,y_sol+60*niv+1, 1)                           #le toit pour finir

if __name__ == '__main__': 
    immeuble(-300,-200)
   
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
