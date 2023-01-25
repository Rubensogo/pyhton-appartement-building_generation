import  turtle
from rectangle import rectangle

def porte2(x,y,couleur):

    turtle.fillcolor(couleur)   #création du rectangle + remplissage + positionnement pour le demi-cercle
    turtle.begin_fill()
    rectangle(x,y,30,40)
    turtle.end_fill()
    turtle.forward(30) 
    turtle.left(90)
    turtle.forward(40) 
    turtle.end_fill()


    turtle.fillcolor(couleur)  #création du demi-cercle
    turtle.begin_fill()
    turtle.circle(15,180)
    turtle.left(90)
    turtle.end_fill()
    turtle.pencolor(couleur)
    turtle.forward(30)
    turtle.pencolor("black")
    
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte dont le haut est un demi cercle
        La porte a une largeur totale de 30 pixels
        La partie rectangulaire a une hauteur de 40 pixels
        La partie semi circulaire a un rayon de 15 pixels
    '''
    pass

if __name__ == '__main__':
    porte2(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()