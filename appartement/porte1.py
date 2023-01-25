import turtle
from rectangle import rectangle

def porte1(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    Remarque:
        Cette fonction dessine une porte pleine
        La porte a une largeur totale de 30 pixels
        et une hauteur de 50 pixels
    '''
    turtle.begin_fill()    #Fonction remplissage
    turtle.fillcolor(couleur)  #choix couleur
    rectangle(x,y,30,50)    #Utilisation de la fonction rectangle déjà faite en donnant les bonnes coordonnées
    turtle.end_fill()        #Fin du remplissage
    pass

if __name__ == '__main__':
    porte1(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()