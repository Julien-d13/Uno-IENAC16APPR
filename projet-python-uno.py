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
import time
import copy as cp
from tkinter import *   

###################################################################
# Fonctions
###################################################################

def a_qui_le_tour(sens,joueur_qui_joue,nbr,passe):
    if passe[0] == 'no':
        if sens[0] == 'droite' :
            if joueur_qui_joue == nbr-1:
                joueur_qui_joue = 0
            else:
                joueur_qui_joue = joueur_qui_joue +1
        else:
            if joueur_qui_joue == 0:
                joueur_qui_joue = nbr-1
            else:
                joueur_qui_joue = joueur_qui_joue - 1
    else:
        if sens[0] == 'droite' :
            if joueur_qui_joue == nbr-1:
                joueur_qui_joue = 1
            elif joueur_qui_joue == nbr-2:
                joueur_qui_joue = 0
            else:
                joueur_qui_joue = joueur_qui_joue +2
        else:
            if joueur_qui_joue == 0:
                joueur_qui_joue = nbr-2
            elif joueur_qui_joue == 1:
                joueur_qui_joue = nbr-1
            else:
                joueur_qui_joue = joueur_qui_joue - 2 
    return joueur_qui_joue
    
    
    
def choix_cartes(nbr,jeu_de_cartes, joueur_qui_joue, fausse, cartes_joueurs):
    print('Vos cartes sont :',cartes_joueurs[0])
    print()
    print("Choisissez la carte à déposer [1, 2, 3, ...]")
    print("Entrez 0 pour piocher")
    choix = int(input())
    choix = choix - 1
    
    while choix>len(cartes_joueurs[0])-1 or choix < -1:
        print("Vous avez fait une faute de frappes, l'indice choisi est trop élévé")
        print('Choisissez la carte à déposer [1, 2, 3, ...]')
        print("Entrez 0 pour piocher")
        choix=int(input())
        choix = choix - 1
        #revoir les possibilités pour le choix : pas jolie de mettre le -1
        
    if choix == -1:
        pioche(0, cartes_joueurs, jeu_de_cartes,1)
        print('Vous avez pioché', cartes_joueurs[0][0])
        if test_carte(cartes_joueurs[0][0], fausse, joueur_qui_joue, nbr) == True:
            depose_carte(cartes_joueurs[0][0],joueur_qui_joue, sens, nbr,cartes_joueurs)
            print("Bonne Pioche ! Vous jouez", cartes_joueurs[0][0])
            del cartes_joueurs[0][0]
            
    else:
        carte_jouée=cartes_joueurs[0][choix]
        if test_carte(carte_jouée,fausse, joueur_qui_joue, nbr)  == False:
            print("Mauvais choix")
            choix_cartes(nbr,jeu_de_cartes, joueur_qui_joue, fausse, cartes_joueurs)
        else:
            depose_carte(cartes_joueurs[0][choix],joueur_qui_joue, sens, nbr, cartes_joueurs)
            print("Vous jouez", cartes_joueurs[0][choix])
            del cartes_joueurs[0][choix]


    
def creation_jeu_de_cartes():
    B = ['B 0']
    for i in range(1,10):
        i = str(i)
        B.append('B '+i)
        B.append('B '+i)
    B = B+ ['B +2']*2 + ['B Passe']*2 + ['B Inverse']*2
    
    R=['R 0']
    for i in range(1,10):
        i = str(i)
        R.append('R '+i)
        R.append('R '+i)
    R = R+ ['R +2']*2 + ['R Inverse']*2 + ['R Passe']*2 
    
    V = ['V 0']
    for i in range(1,10):
        i=str(i)
        V.append('V '+i)
        V.append('V '+i)
    V = V + ['V +2']*2 + ['V Passe']*2 +['V Inverse']*2
    
    J = ['J 0']
    for i in range(1,10):
        i=str(i)
        J.append('J '+i)
        J.append('J '+i)
    J = J+['J Passe']*2 + ['J Inverse']*2 + ['J +2']*2
    
    Joker = ['Joker']*4
    Super_Joker = ['Joker +4']*4
    
    jeu_de_cartes = B  + R + V + J + Super_Joker + Joker
    
    shuffle(jeu_de_cartes)
    
    return jeu_de_cartes
    
    
    
def depose_carte(carte_jouée,joueur_qui_joue, sens, nbr,cartes_joueurs):
    if carte_jouée =='Joker':
        print('Choisissez une couleur')
        couleur=input('R,B,V,J ?  ')
        while couleur!= 'R' and couleur != 'B' and couleur!= 'V' and couleur!= 'J' :
            print('Faute de frappe')
            print('choisissez une couleur')
            couleur=input('R,B,V,J ?  ')
        couleur=couleur + '   ' # permet de gérer les test sur les cartes minimum de longueur 3
        fausse.insert(0,carte_jouée)
        fausse.insert(0,str(couleur))
        
    elif carte_jouée == 'Joker +4':
        print('Choisissez une couleur')
        couleur=input('R,B,V,J ?   ')
        while couleur!= 'R' and couleur != 'B' and couleur!= 'V' and couleur!= 'J' :
            print('Faute de frappe')
            print('choisissez une couleur')
            couleur = input('R,B,V,J ?  ')
        couleur = couleur + '   ' 
        fausse.insert(0,carte_jouée)
        fausse.insert(0,str(couleur))
        joueur_qui_pioche = a_qui_le_tour(sens,joueur_qui_joue,nbr,passe)
        pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,4)
        
    elif carte_jouée[2] == '+': # seul les cartes +2 ont cette possibilité, si carte jouée = carte +2 
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            fausse.insert(0,carte_jouée)
            joueur_qui_pioche = a_qui_le_tour(sens,joueur_qui_joue,nbr,passe)
            pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,2)
            
    elif carte_jouée[2] == 'I':
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            sens.reverse()
            fausse.insert(0,carte_jouée)
    elif carte_jouée[2] == 'P':
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:    
            passe.reverse()
            fausse.insert(0,carte_jouée)
    else:
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            fausse.insert(0,carte_jouée)
    


def depose_carte_IA(carte_jouée,joueur_qui_joue, sens, nbr,cartes_joueurs):
    if carte_jouée =='Joker':
        V=0
        J=0
        R=0
        B=0
        for i in range(len(cartes_joueurs[joueur_qui_joue])):
            if cartes_joueurs[joueur_qui_joue][i][0] == 'V':
                V += 1
            if cartes_joueurs[joueur_qui_joue][i][0] == 'J':
                J += 1
            if cartes_joueurs[joueur_qui_joue][i][0] == 'R':
                R += 1
            if cartes_joueurs[joueur_qui_joue][i][0] == 'B':
                B += 1
        maxi = max(V,J,R,B)
        if R == maxi:
            couleur = 'R'
        elif V == maxi:
            couleur = 'V'
        elif J == maxi:
            couleur = 'J'
        elif B == maxi:
            couleur = 'B'
        else:
            n = randint(0,3)
            if n == 0:
                couleur = 'V'
            if n == 1:
                couleur = 'J'
            if n == 2:
                couleur = 'R'
            if n == 3:
                couleur = 'B'
        couleur=couleur + '   '
        fausse.insert(0,carte_jouée)
        fausse.insert(0,str(couleur))
        
    elif carte_jouée == 'Joker +4':
        V=0
        J=0
        R=0
        B=0
        for i in range(len(cartes_joueurs[joueur_qui_joue])):
            if cartes_joueurs[joueur_qui_joue][i][0] == 'V':
                V += 1
            if cartes_joueurs[joueur_qui_joue][i][0] == 'J':
                J += 1
            if cartes_joueurs[joueur_qui_joue][i][0] == 'R':
                R += 1
            if cartes_joueurs[joueur_qui_joue][i][0] == 'B':
                B += 1
        maxi = max(V,J,R,B)
        if R == maxi:
            couleur = 'R'
        elif V == maxi:
            couleur = 'V'
        elif J == maxi:
            couleur = 'J'
        elif B == maxi:
            couleur = 'B'
        else:
            n = randint(0,3)
            if n == 0:
                couleur = 'V'
            if n == 1:
                couleur = 'J'
            if n == 2:
                couleur = 'R'
            if n == 3:
                couleur = 'B'
        couleur=couleur + '   '
        fausse.insert(0,carte_jouée)
        fausse.insert(0,str(couleur))
        joueur_qui_pioche = a_qui_le_tour(sens,joueur_qui_joue,nbr,passe)
        pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,4)
        
    elif carte_jouée[2] == '+': # seul les cartes +2 ont cette possibilité, si carte jouée = carte +2 
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            fausse.insert(0,carte_jouée)
            joueur_qui_pioche = a_qui_le_tour(sens,joueur_qui_joue, nbr, passe)
            pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,2)
            
    elif carte_jouée[2] == 'I':
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            sens.reverse()
            fausse.insert(0,carte_jouée)
            
    elif carte_jouée[2] == 'P':
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:    
            passe.reverse()
            fausse.insert(0,carte_jouée)
    else:
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            fausse.insert(0,carte_jouée)
            
            
    
def distribution(nbr, jeu_de_cartes):
    cartes_joueurs = []
    
    for i in range(0,nbr):
        cartes_joueurs.append([0]*7) #creation d'une liste de liste pouvant contenir les cartes des joueurs
        
    for j in range(7):
        for k in range(0,nbr):
            cartes_joueurs[k][j] = jeu_de_cartes[0]
            del jeu_de_cartes[0]
            
    return cartes_joueurs
    


def fausse(jeu_de_cartes):
    fausse = []
    while jeu_de_cartes[0] == 'Joker' or jeu_de_cartes[0] == 'Joker +4' or jeu_de_cartes[0][2] == 'I' or jeu_de_cartes[0][2] == 'P' or jeu_de_cartes[0][2] == '+':
        mem = jeu_de_cartes[0]
        jeu_de_cartes.append(mem)
        del jeu_de_cartes[0]
    fausse.append(jeu_de_cartes[0])
    del jeu_de_cartes[0]
    return fausse
    


def IA(nbr,jeu_de_cartes, joueur_qui_joue, fausse, cartes_joueurs):
    i=0
    j=0
    
    while test_carte(cartes_joueurs[joueur_qui_joue][i], fausse, joueur_qui_joue, nbr) == False and j !=1 :
        i = i+1
        if i >= len(cartes_joueurs[joueur_qui_joue]):
            i=i-1
            j=1
            
    if j == 0:
        print('Il a joué', cartes_joueurs[joueur_qui_joue][i])
        depose_carte_IA(cartes_joueurs[joueur_qui_joue][i],joueur_qui_joue, sens, nbr,cartes_joueurs)
        del cartes_joueurs[joueur_qui_joue][i]
        
    else:
        print('Il pioche')
        pioche(joueur_qui_joue, cartes_joueurs, jeu_de_cartes,1)
        if test_carte(cartes_joueurs[joueur_qui_joue][0], fausse, joueur_qui_joue, nbr) == True:
            print('Bonne pioche !', cartes_joueurs[joueur_qui_joue][0])
            depose_carte_IA(cartes_joueurs[joueur_qui_joue][0],joueur_qui_joue, sens, nbr, cartes_joueurs)
            del cartes_joueurs[joueur_qui_joue][0]



def jeu(nbr,jeu_de_cartes, joueur_qui_joue, fausse, liste_joueurs, cartes_joueurs):
        print()
        print()
        if liste_joueurs[joueur_qui_joue] == 'Joueur 1':
            print("A vous de jouer Joueur 1")
            print( "La carte du dessus est ", fausse[0])
            choix_cartes(nbr,jeu_de_cartes, joueur_qui_joue, fausse, cartes_joueurs)
        else:
            print("C'est au tour de", liste_joueurs[joueur_qui_joue], "de jouer")
            print( "La carte du dessus est ", fausse[0])
            IA(nbr,jeu_de_cartes, joueur_qui_joue, fausse, cartes_joueurs)
    
    
    
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


     
def qui_commence(nbr,liste_joueurs):
    joueur_qui_commence=randint(0,nbr -1)
    return joueur_qui_commence    
        


def pioche(joueur_qui_pioche, cartes_joueurs, jeu_de_cartes,nb_carte_pioche):
    for k in range(nb_carte_pioche):
        cartes_joueurs[joueur_qui_pioche].insert(0,jeu_de_cartes[0])
        del jeu_de_cartes[0]
        
        
        
def test_carte(carte_jouée,fausse, joueur_qui_joue, nbr):
    if carte_jouée =='Joker':
        if fausse[0] == 'Joker +4':
            return False
        else:
            return True
    elif carte_jouée == 'Joker +4':
        if fausse[0] == 'Joker +4':
            return False
        else:
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
    elif carte_jouée[2] == 'P':
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:    
            return True
        else:
            return False
    else:
        if carte_jouée[0] == fausse[0][0] or carte_jouée[2] == fausse[0][2]:
            return True
        else:
            return False 
            
            

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
        return True
        
    else:
        return False
        
        
    #Mettre un +2 sur un autre +2
    #Interface graphique
    #Compter les points
        

    

###################################################################
# Script principal de test
###################################################################

liste_joueurs = liste_joueurs()
nbr = len(liste_joueurs)
jeu_de_cartes = creation_jeu_de_cartes()
cartes_joueurs = distribution(nbr, jeu_de_cartes)

joueur_qui_joue = qui_commence(nbr,liste_joueurs)
joueur_qui_commence = liste_joueurs[joueur_qui_joue]

fausse = fausse(jeu_de_cartes)

sens = ['droite','gauche']
passe = ['no','yes']


while test_gagnant(cartes_joueurs, nbr, liste_joueurs) == False:
    if len(jeu_de_cartes)<5:
        mem = [fausse[0]]
        del fausse[0]
        i=0
        while i<len(fausse):
            if len(fausse[i]) == 4: # on supprime les cartes couleurs
                del fausse[i]
            i=i+1
        shuffle(fausse)
        jeu_de_cartes = jeu_de_cartes + fausse
        fausse=mem
    jeu(nbr,jeu_de_cartes, joueur_qui_joue, fausse, liste_joueurs, cartes_joueurs)
    if test_gagnant(cartes_joueurs, nbr, liste_joueurs) == False:
        if len(cartes_joueurs[joueur_qui_joue]) == 1:
            print(liste_joueurs[joueur_qui_joue], "dit : UNO !")
            joueur_qui_joue = a_qui_le_tour(sens, joueur_qui_joue,nbr,passe)
            passe = ['no','yes']
        else:
            joueur_qui_joue = a_qui_le_tour(sens, joueur_qui_joue,nbr,passe)
            passe = ['no','yes']
    else:
        print("Le gagnant est : ", liste_joueurs[joueur_qui_joue])
    print()
    print()
    print("---------------------------------------------------------------------------------")
    time.sleep(3)




#probleme pour remettre le jeu de cartes à 0 lorsqu'il n'a presque plus de cartes
#si on ne trouve pas de solution on réduira le nombre de joueurs à 4
 