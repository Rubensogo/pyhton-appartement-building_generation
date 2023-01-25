import turtle

def rectangle(x,y,w,h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    '''
    turtle.penup()
    turtle.goto(x,y) #positionne le curseur
    turtle.pendown()

    for i in range (2):
        turtle.forward(w) # Déplace la tortue de w unités vers l'avant
        turtle.left(90) # rotation de la tortue de 90 degrés
        turtle.forward(h) # Déplace la tortue de h unités vers l'avant
        turtle.left(90) # rotation de la tortue de 90 degrés

if __name__ == '__main__':
    rectangle(0,0,150,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()