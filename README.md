# CryptageC-sare
Un code en python pour le cryptage de Césare

1 - Importation de modules :
import string
Ici, le module string est importé pour utiliser la constante string.ascii_uppercase, qui représente toutes les lettres majuscules de l'alphabet.

2 - Définition des fonctions de chiffrement et de déchiffrement :
    def chiffrement_cesare(texte, cle):
        a - texte = texte.upper() :
        Convertit le texte en majuscules. Cela assure que le chiffrement est effectué de manière insensible à la casse.
        b - alphabet = string.ascii_uppercase :
        Crée une chaîne contenant toutes les lettres majuscules de l'alphabet.
        c - cle = int(cle) :
        Convertit la clé (décalage dans le chiffrement de César) en un entier. Cela est nécessaire car l'entrée utilisateur est traitée comme une chaîne de caractères.
        d - tableau_chiffrement = str.maketrans(alphabet, alphabet[cle:] + alphabet[:cle]) :
        Utilise la fonction str.maketrans pour créer une table de substitution. Elle mappe chaque caractère de l'alphabet vers le caractère correspondant après le décalage.
        e - texte_chiffre = texte.translate(tableau_chiffrement) :
        Utilise la méthode translate pour appliquer la substitution à chaque caractère du texte.
        f - return texte_chiffre : Renvoie le texte chiffré.

    def dechiffrement_cesare(texte_chiffre, cle):
        a - texte_chiffre = texte_chiffre.upper() :
        Convertit le texte chiffré en majuscules pour assurer la correspondance avec l'alphabet.
        b - alphabet = string.ascii_uppercase : Initialise l'alphabet.
        c - cle = int(cle) : Convertit la clé en un entier.
        d - tableau_dechiffrement = str.maketrans(alphabet[cle:] + alphabet[:cle], alphabet) : Crée une table de substitution pour le déchiffrement.
        e - texte = texte_chiffre.translate(tableau_dechiffrement) : Applique la substitution au texte chiffré pour obtenir le texte déchiffré.
        f - return texte : Renvoie le texte déchiffré.


Ces fonctions prennent un texte et une clé en entrée, puis effectuent le chiffrement ou le déchiffrement de César en utilisant une table de substitution.

3 - Conversion de la clé en entier :
cle = int(cle)
Cette ligne de code convertit la clé (qui est une chaîne de caractères obtenue à partir de l'entrée utilisateur) en un entier. Cela est nécessaire car les indices pour le découpage de la chaîne doivent être des entiers.

4 - Logique de l'interface utilisateur :
def cryptage_cesare() :
def cryptage_cesare():
    # ...
Cette fonction affiche un menu à l'utilisateur avec les options de chiffrement et de déchiffrement. En fonction du choix de l'utilisateur, elle demande le texte et la clé appropriés, puis appelle la fonction de chiffrement ou de déchiffrement.

    a - choice = int(input('Faites votre choix : '))
Cette ligne de code convertit le choix de l'utilisateur en un entier. Cela est nécessaire car input() renvoie une chaîne de caractères, et vous devez comparer le choix avec des entiers dans les instructions conditionnelles.


    b - print('Veuillez faire un choix entre 1 et 2')
Cette ligne affiche un message d'erreur lorsque l'utilisateur entre un choix invalide.

5 - Appel de la fonction principale :
cryptage_cesare()
Enfin, cette ligne appelle la fonction principale pour exécuter le programme.
