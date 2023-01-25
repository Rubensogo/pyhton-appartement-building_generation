# Module par sebastien chanthery

import turtle
from trait import trait

# ----- Sol de la rue -----
def sol(y_sol):
    turtle.pensize(3)      #un grand trait épais
    turtle.penup()
    trait(-400, y_sol, 400, y_sol)
    turtle.pensize(1)
    

    '''
    Paramètres
        y_sol : ordonnée du sol du la rue
    Cete fonction dessine un trait horizontale de 3 pixels d'épaisseur
    '''

    pass


if __name__ == '__main__':
    sol(-300)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
