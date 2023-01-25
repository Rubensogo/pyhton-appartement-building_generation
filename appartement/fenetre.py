from rectangle import rectangle
import turtle

def fenetre(x,y):
    turtle.penup()
    turtle.goto(x,y) #positionne le curseur
    turtle.pendown()
    turtle.fillcolor("white")  #remplissage en blanc pour les fenêtres
    turtle.begin_fill()         #Fonction remplissage 
    rectangle (x, y, 30, 30)    #Utilisation de la fonction rectangle déjà faite en donnant les bonnes coordonnées
    turtle.end_fill()           #Fin du remplissage
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    pass

if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()