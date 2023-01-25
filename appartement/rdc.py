from facade import facade
import random 
from porte import porte
from fenetre import fenetre
import turtle

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''

    # Dessine la facade
    facade(x,y_sol,c_facade,1)  

    # création aléatoire du rdc suivant la position aléatoire de la porte
    place = random.randint(1,3)
    print(place)
    if place == 1:
        porte(x+15,y_sol+0,c_porte)
        fenetre(x+55,y_sol+20)
        fenetre(x+95,y_sol+20)
    if place == 2:
        porte(x+55,y_sol+0,c_porte)
        fenetre(x+15,y_sol+20)
        fenetre(x+95,y_sol+20)
    if place == 3:
        porte(x+95,y_sol+0,c_porte)
        fenetre(x+15,y_sol+20)
        fenetre(x+55,y_sol+20)


    

if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()