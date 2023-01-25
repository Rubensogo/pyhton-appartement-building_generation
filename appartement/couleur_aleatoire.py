import turtle
import random

def couleur_aleatoire():
    '''
    renvoie un triplet de 3 nombres entier compris entre 0 et 255
    Ce triplet correspond à une couleur codée en RVB
    '''

   
    liste_de_couleur = ["blue", "red", "green", "grey", "pink", "brown", "yellow", "navy", "orange", "gold", "tan", "sienna", "wheat", "cyan", "salmon", "violet", "purple"]
    #choisi un nombre entre 1 et 19
    n = random.randint(0, 16)
    #prend un element de la liste_de_couleur
    couleur = liste_de_couleur[n]
    return couleur

couleur_aleatoire()


"""
    #géneration aléatoire de 3 valeurs entre 0 et 255 pour code RGB
    rouge = random.randint(0,255)
    vert = random.randint(0,255)
    bleu = random.randint(0,255)

    #Assemble toutes les valeurs pour créer le code
    random_couleur = (rouge, vert, bleu )
    return random_couleur
"""








