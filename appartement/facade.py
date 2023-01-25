from textwrap import fill
import turtle
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
    turtle.penup()
    turtle.goto(x,y_sol*niveau)                 #Placement de la tortue
    turtle.pendown()

    turtle.fillcolor(couleur)                  #Fonction de remplissage + choix couleur
    turtle.begin_fill()

    rectangle(x,y_sol*niveau,140,60)           #Utilisation de la fonction rectangle déjà faite en donnant les bonnes coordonnées
    turtle.end_fill()

if __name__ == '__main__':
    facade(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
