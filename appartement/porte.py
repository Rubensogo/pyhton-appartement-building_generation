import turtle
import random
from porte1 import porte1
from porte2 import porte2

def porte(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte au hasard entre porte1 et porte2
    '''
    pass

    choix=random.randint(0,1) #appel aléatoire de la porte1 ou la porte2
    if choix==0:
        porte1(x,y,couleur)
    if choix==1:
        porte2(x,y,couleur)




if __name__ == '__main__':
    porte(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
