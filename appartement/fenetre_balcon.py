from textwrap import fill
import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    turtle.fillcolor("white")            #couleur blanche pour la fenêtre
    turtle.begin_fill()                   #Fonction remplissage                       
    rectangle (x,y, 30, 50)               #Utilisation de la fonction rectangle déjà faite en donnant les bonnes coordonnées
    turtle.end_fill()                     #Fin du remplissage
    # porte-fenetre

    pass
    turtle.fillcolor("white")           #couleur blanche pour la fenêtre
    turtle.begin_fill()                  #Fonction remplissage 
    turtle.pensize(2)                    #Augmentation de la taille du trait
    rectangle(x-3, y, 38, 25)            #Utilisation de la fonction rectangle déjà faite en donnant les bonnes coordonnées
    for i in range (4):                   #Boucle pour faire les barreaux du balcon
        turtle.forward(5)
        turtle.left(90)
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)
        turtle.forward(25)
        turtle.left(90)
    turtle.end_fill()                    #Fin du remplissage
    turtle.pensize(1)                    #Remettre bien la taille du trait
    # balcon


    pass



if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()