# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 09:35:04 2023

@author: Sufyane Ramseyn 
"""

import string


def chiffrement_cesare(texte, cle):
    texte = texte.upper()
    alphabet = string.ascii_uppercase
    cle = int(cle)
    tableau_chiffrement = str.maketrans(alphabet, alphabet[cle:] + alphabet[:cle])
    texte_chiffre = texte.translate(tableau_chiffrement)
    return texte_chiffre

def dechiffrement_cesare(texte_chiffre, cle):
    texte_chiffre = texte_chiffre.upper()
    alphabet = string.ascii_uppercase
    cle = int(cle)
    tableau_dechiffrement = str.maketrans(alphabet[cle:] + alphabet[:cle], alphabet)
    texte = texte_chiffre.translate(tableau_dechiffrement)
    return texte


def cryptage_cesare():
    print('1 - Chiffrement Césare')
    print('2 - Déchiffrement Césare')
    choice = int(input('Faites votre choix : '))
    
    if choice == 1:
        text = input("Veuillez saisir le texte à crypter : ")
        key = input("Veuillez saisir la clé de cryptage : ")
        texte_chiffrer = chiffrement_cesare(text, key)
        print(texte_chiffrer)
    elif choice == 2:
        texte = input("Veuillez saisir le texte crypté : ")
        cle = input("Veuillez saisir la clé de décryptage : ")
        texte_dechiffrer = dechiffrement_cesare(texte, cle)
        print(texte_dechiffrer)
    else:
        print('Veuillez faire un choix entre 1 et 2')

cryptage_cesare()
