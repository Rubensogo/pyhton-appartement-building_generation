import turtle


def toit1(x, y_sol, niveau):
    
    turtle.penup()
    turtle.goto(x,y_sol*niveau)
    turtle.pendown()   #création d'un triangle isocèle
    turtle.penup()
    turtle.goto(x,y_sol*niveau)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.forward (80) 
    turtle.left (143.13)
    turtle.forward (100)
    turtle.left (73.74)
    turtle.forward (101)
    turtle.end_fill()
    turtle.left (143.13)  #Remettre bien la turtle pour enchainer avec un autre immeuble
    
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    pass


if __name__ == '__main__':
    toit1(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()