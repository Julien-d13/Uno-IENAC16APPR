###################################################################
# Fichier projet-python-uno.py
# Projet python semestre 6
# BITTERMANN Hugo, LOUISE Romain et RAPIN Julien - Date de début : 06/06/2017 - Date de fin :
###################################################################


###################################################################
# Importations
###################################################################

from random import *
from numpy import *

###################################################################
# Fonctions
###################################################################

def liste_joueurs():
    player = []
    print("A combien voulez-vous jouer ?")
    a = int(input())
    if a < 2 or a > 10:
        print("Le uno se joue de 2 à 10 joueurs.")
        player = nbr_joueurs()
    else:
        for i in range(1,a+1):
            i=str(i)
            player.append('Joueur ' + i)
    return player
    

def creation_jeu_de_cartes():
    B = ['B 0']
    for i in range(1,10):
        i = str(i)
        B.append('B '+i)
        B.append('B '+i)
    B = B+['B Passe']*2 + ['B +2']*2 + ['B Inverse']*2
    
    R=['R 0']
    for i in range(1,10):
        i = str(i)
        R.append('R '+i)
        R.append('R '+i)
    R = R+['R Passe']*2 + ['R +2']*2 + ['R Inverse']*2
    
    V = ['V 0']
    for i in range(1,10):
        i=str(i)
        V.append('V '+i)
        V.append('V '+i)
    V = V+['V Passe']*2 + ['V +2']*2 + ['V Inverse']*2
    
    J = ['J 0']
    for i in range(1,10):
        i=str(i)
        J.append('J '+i)
        J.append('J '+i)
    J = J+['J Passe']*2 + ['J +2']*2 + ['J Inverse']*2
    
    Joker = ['Joker']*4
    Super_Joker = ['Joker +4']*4
    
    jeu_de_cartes = B  + R + V + J + Super_Joker + Joker
    
    shuffle(jeu_de_cartes)
    
    return jeu_de_cartes
    
    
def distribution(nbr, jeu_de_cartes):
    cartes_joueurs = []
    for i in range(0,nbr):
        cartes_joueurs.append([0]*108) #creation d'une liste de liste pouvant contenir les cartes des joueurs
    for j in range(7):
        for k in range(0,nbr):
            cartes_joueurs[k][j] = jeu_de_cartes[0]
            del jeu_de_cartes[0]
    return cartes_joueurs
     
def qui_commence(nbr,liste_joueurs):
    joueur_qui_commence=randint(0,nbr -1)
    joueur_commencant = liste_joueurs[joueur_qui_commence]
    return joueur_commencant      
        
def fausse(jeu_de_cartes):
    fausse = []
    fausse.append(jeu_de_cartes[0])
    return fausse
    
def afficher_cartes(cartes_joueurs):
    i = 0
    cartes_utilisateur = []
    while cartes_joueurs[0][i]!= 0:
        cartes_utilisateur.append(cartes_joueurs[0][i])
        i = i+1
    return cartes_utilisateur

def test_gagnant(cartes_joueurs, nbr, liste_joueurs):
    i=0
    j=0
    while cartes_joueurs[i]!=[0]*108 and j<nbr:
        j=j+1
        if j<nbr:
            i=j
        else:
            i=j-1
    if j != nbr:
        return True #il faudra retourner le nom du dernier joueur pour définir le gagnant
    else:
        return False
    

def jeu(nbr,jeu_de_cartes, joueur_qui_commence, fausse, liste_joueurs, cartes_joueurs):
    


        
    
###################################################################
# Script principal de test
###################################################################

liste_joueurs = liste_joueurs()
nbr = len(liste_joueurs)
jeu_de_cartes = creation_jeu_de_cartes()
cartes_joueurs = distribution(nbr, jeu_de_cartes)
cartes_utilisateur = afficher_cartes(cartes_joueurs)
print('Vos cartes sont :',cartes_utilisateur)
joueur_qui_commence = qui_commence(nbr,liste_joueurs)
print('Le joueur débutant la partie est le ',joueur_commencant)
print()
print()
fausse = fausse(jeu_de_cartes)
print( "La carte du dessus est ", fausse)


if joueur_qui_commence=='Joueur 1':
    print("A vous de jouer")
    print("Choisissez la carte à déposer")
    print("Il faut sélectionner l emplacement dans la liste de la carte désirée")
    print("Quel est votre choix")
    choix=int(input())
    while choix>len(cartes_utilisateur)-1:
        print('Vous avez fait une faute de frappes, l indice choisi est trop élévé')
        print('Quel est votre choix ?")
        choix=int(input())

else:
    


    
test_gagnant(cartes_joueurs, nbr, liste_joueurs)
while test_gagnant==False:
    jeu(nbr,jeu_de_cartes, joueur_qui_commence, fausse, liste_joueurs, cartes_joueurs)
#retourner le nom du dernier joueur






 