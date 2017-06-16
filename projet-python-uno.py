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
        player = liste_joueurs()
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
        cartes_joueurs.append([0]*7) #creation d'une liste de liste pouvant contenir les cartes des joueurs
    for j in range(7):
        for k in range(0,nbr):
            cartes_joueurs[k][j] = jeu_de_cartes[0]
            del jeu_de_cartes[0]
    return cartes_joueurs
     
def qui_commence(nbr,liste_joueurs):
    joueur_qui_commence=randint(0,nbr -1)
    return joueur_qui_commence    
        
def fausse(jeu_de_cartes):
    fausse = []
    fausse.append(jeu_de_cartes[0])
    return fausse
    
# def afficher_cartes(cartes_joueurs):
#     i = 0
#     cartes_utilisateur = []
#     while cartes_joueurs[0][i]!= 0:
#         cartes_utilisateur.append(cartes_joueurs[0][i])
#         i = i+1
#     return cartes_utilisateur

def test_gagnant(cartes_joueurs, nbr, liste_joueurs):
    i=0
    j=0
    while cartes_joueurs[i]!=[] and j<nbr:
        j=j+1
        if j<nbr:
            i=j
        else:
            i=j-1
    if j != nbr:
        return True #il faudra retourner le nom du dernier joueur pour définir le gagnant
    else:
        return False
        
def a_qui_le_tour(sens,joueur_qui_joue):
    if sens == 'droite' :
        if joueur_qui_joue == nbr-1:
            joeur_qui_joue = 0
        else:
            joeur_qui_jouer = joueur_qui_joue +1
    else:
        if joueur_qui_joue == 0:
            joeur_qui_joue = nbr-1
        else:
            joeur_qui_joue = joueur_qui_joue - 1
    return joueur_qui_joue
        
def pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,nb_carte_pioche):
    for k in range(nb_carte_pioche):
        cartes_joueurs[joueur_qui_joue].append(jeu_de_cartes[0])
        del jeu_de_cartes[0]
    
def depose_carte(carte_jouée,joueur_qui_joue, sens, nbr,cartes_joueurs):
    if carte_jouée =='Joker':
        print('Choisissez une couleur')
        couleur=input('R,B,V,J ?')
        while couleur!= R or couleur != B or couleur!= V or couleur!= J :
            print('Faute de frappe')
            print('choisissez une couleur')
            couleur=input('R,B,V,J ?')
        fausse.append(carte_jouée)
        fausse.append(str(couleur))
    elif carte_jouée == 'Joker +4':
        print('Choisissez une couleur')
        couleur=input('R,B,V,J ?')
        while couleur!= R or couleur != B or couleur!= V or couleur!= J :
            print('Faute de frappe')
            print('choisissez une couleur')
            couleur=input('R,B,V,J ?')
        fausse.append(carte_jouée)
        fausse.append(str(couleur))
        joueur_qui_pioche = a_qui_le_tour(sens,joueur_qui_joue)
        pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,4)
    elif carte_jouée[2] == '+': #seul les cartes +2 ont cette possibilité, si carte jouée = carte +2 
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            fausse.append(carte_jouée)
            joeur_qui_pioche = a_qui_le_tour(sens,joueur_qui_joue)
            pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,2)
    elif carte_jouée[2] == 'I':
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            if sens == 'droite':
                fausse.append(carte_jouée)
                sens = 'gauche'
            else:
                fausse.append(carte_jouée)
                sens = 'droite'
    else:
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            fausse.append(carte_jouée)
    

def test_carte(carte_jouée,fausse, joeur_qui_joue, sens, nbr):
    if carte_jouée =='Joker':
        return True
    elif carte_jouée == 'Joker +4':
        return True
    elif carte_jouée[2] == '+': #seul les cartes +2 ont cette possibilité, si carte jouée = carte +2 
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            return True
        else:
            return False 
    elif carte_jouée[2] == 'I':
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:    
            return True
        else:
            return False
    else:
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            return True
        else:
            return False 
            
            
def choix(nbr,jeu_de_cartes, joueur_qui_joue, fausse, liste_joueurs, cartes_joueurs):
    print("A vous de jouer")
    cartes_utilisateur=afficher_cartes(cartes_joueurs)
    print('Vos cartes sont :',cartes_utilisateur)
    print("Choisissez la carte à déposer")
    print("Il faut sélectionner l emplacement dans la liste de la carte désirée")
    print("Quel est votre choix")
    print("Si vous ne pouvez pas jouer, entrez -1")
    choix=int(input())
    while choix>len(cartes_utilisateur)-1:
        print('Vous avez fait une faute de frappes, l indice choisi est trop élévé')
        print('Quel est votre choix ?')
        choix=int(input())
        #revoir les possibilités pour le choix : pas jolie de mettre le -1
    if choix == -1:
        pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,1)
        if test_carte(cartes_utilisateur[0], joueur_qui_joue, sens, nbr) == True:
            depose_carte(carte_utilisateur[0],joueur_qui_joue, sens, nbr)
            del cartes_utilisateur[0]
        else:
            joueur_qui_joue = a_qui_le_tour(sens,joueur_qui_joue)
    else:
        carte_jouée=cartes_utilisateur[choix]
        test = test_carte(carte_jouée,fausse, joeur_qui_joue, sens, nbr) 
        while test == False:
            choix(nbr,jeu_de_cartes, joueur_qui_joue, fausse, liste_joueurs, cartes_joueurs)
        depose_carte(carte_utilisateur[0],joueur_qui_joue, sens, nbr)


def jeu(nbr,jeu_de_cartes, joueur_qui_joue, fausse, liste_joueurs, cartes_joueurs):
    if liste_joueurs[joueur_qui_joue] == 'Joueur 1':
        print("A vous de jouer")
        cartes_utilisateur=afficher_cartes(cartes_joueurs)
        print('Vos cartes sont :',cartes_utilisateur)
        print("Choisissez la carte à déposer")
        print("Il faut sélectionner l emplacement dans la liste de la carte désirée")
        print("Quel est votre choix")
        print("Si vous ne pouvez pas jouer, entrez -1")
        choix=int(input())
        while choix>len(cartes_utilisateur)-1:
            print('Vous avez fait une faute de frappes, l indice choisi est trop élévé')
            print('Quel est votre choix ?')
            choix=int(input())
            #revoir les possibilités pour le choix : pas jolie de mettre le -1
        if choix == -1:
            pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,1)
            if test_carte(cartes_utilisateur[0], joueur_qui_joue, sens, nbr) == True:
                depose_carte(carte_utilisateur[0],joueur_qui_joue, sens, nbr)
                del cartes_utilisateur[0]
            else:
                joueur_qui_joue) = a_qui_le_tour(sens,joueur_qui_joue)
        else:
            carte_jouée=cartes_utilisateur[choix]
            test = test_carte(carte_jouée,fausse, joeur_qui_joue, sens, nbr) 
            while test =! True:
                
                #peut être faut-il créer une fonction choix
        
        # autre boucle pour faire le test et pouvoir redemander un autre choix
        # def test qui test si la carte peut être posée
        # en sortie de test, si la carte a pu être jouée alors supprimer la carte
        #besoin de tester si le paquet de carte est vide si oui, reprendre la fausse, la mélanger et retirer les cartes couleurs
        #choisir si on prend la fonction choix ou non
        #faire attention aux fonctions test et dépose pour l'IA
        
        
###################################################################
# Script principal de test
###################################################################

liste_joueurs = liste_joueurs()
nbr = len(liste_joueurs)
jeu_de_cartes = creation_jeu_de_cartes()
cartes_joueurs = distribution(nbr, jeu_de_cartes)
cartes_utilisateur = cartes_joueurs[0]

joueur_qui_commence = liste_joueurs[qui_commence(nbr,liste_joueurs)]
print('Le joueur débutant la partie est le ',joueur_qui_commence)
print()
print()
fausse = fausse(jeu_de_cartes)
print( "La carte du dessus est ", fausse)
joeur_qui_joue = joueur_qui_commence
sens='droite'




# else:
    
    
test_gagnant(cartes_joueurs, nbr, liste_joueurs)
while test_gagnant==False:
    jeu(nbr,jeu_de_cartes, joueur_qui_commence, fausse, liste_joueurs, cartes_joueurs)
#retourner le nom du dernier joueur






 