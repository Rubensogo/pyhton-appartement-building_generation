import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble

# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(800, 600)
    turtle.speed(100)
    # On définit le x et y de base
    y_sol = -200
    x = -350
    # Dessin du sol de la rue
    sol(y_sol)

    # Dessin des 4 immeubles
    for i in range (4):
        immeuble(x,y_sol)
        x += 180                 #écart de 180 pixel entre les immeubles
        


    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

if __name__ == '__main__':
    main()



