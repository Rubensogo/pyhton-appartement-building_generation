import turtle
from trait import trait

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    turtle.penup()
    turtle.goto(x,y_sol*niveau)
    turtle.pendown()
                                              #juste un trait assez épais
    turtle.pensize(10)                        #Grande augmentation de la police
    turtle.forward(70)                        
    turtle.left(180)
    turtle.forward(140)
    turtle.pensize(1)                           #Remettre bien la police
    turtle.left(180)                         #Remettre bien la turtle pour enchainer avec un autre immeuble
  


if __name__ == '__main__':
    toit2(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()