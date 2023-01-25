from facade import facade
import random
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle

def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs
    facade(x,y_sol,couleur,niveau)  #Appel de la facade pour placer les fenêtres dessus
    # dessin des 3 Eléments
    

    for i in range(3):            #Boucle servant a décaler les fenêtres

        if i == 0:
            x += 15
        else: 
            pass

        type=random.randint(0,1)    # Choix du type de fenêtres entre balcon et sans-balccon
        if type==0:
            fenetre((x+40*i),(y_sol*niveau+20)) #Appel de la fenêtre sans balcon et ajustement des coordonnées par rapport à la facade
        else:
            fenetre_balcon((x+40*i),y_sol*niveau)#Appel de la fenêtre avec balcon et ajustement des coordonnées par rapport à la facade

if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()