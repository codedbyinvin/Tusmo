from random import randint
import unicodedata

def remove_accents(input_liste):
    """Fonction qui permet de rendren une liste de mots avec accent en caractères sans accents
    Arg : une liste de mots 
    Returns : cette liste de mots sans accents
    """
    liste_mots_sans_accents = []
    for word in  input_liste:
        nfkd_form = unicodedata.normalize('NFKD', word)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        encoding = "utf-8"
        unicoded_string = only_ascii.decode(encoding)
        liste_mots_sans_accents.append(unicoded_string)
    return liste_mots_sans_accents

chiffre = randint(0,22741)
#J'ouvre le fichier avec les mots, j'en fais une liste et lui retire ses accents 
# ==> j'ai pas trouvé d'encoding qui permet de  le faire directement
with open("mots-1.txt","r") as data_words:
    liste_mots = data_words.read().splitlines()
liste_mots_sans_accents = remove_accents(liste_mots)
data_words.close()
#-----------------------------------------------------------------------
lifes = 6
word_to_find = liste_mots[chiffre]
size_word_to_find = len(word_to_find)
first_letter_word_to_find = word_to_find[0].upper()
#-----------------------------------------------------------------------
print(f"""----------Bienvenue dans Motus et Bouche cousus :)) ----------
Tu dois trouver un mot de {size_word_to_find} lettres commençant par {first_letter_word_to_find}
Tu as 6 chances""")
while lifes > 0:                                                   #Tant qu'il a des vies, il recommence
    word = input("Veuillez entrer votre mot : ")
    word = word.lower()
    if word not in liste_mots or len(word) != size_word_to_find:   #Si le mot n'est pas de la bonne taille ou qu'il n'est pas dans la liste FAUX
        print("Mot incorrecte")
    else:
        if word == word_to_find:                                    #Quand tu le trouves tu arretes
            print("Bravo tu as trouvé le mot !!")
            break
        else:
            for k in range(1,len(word)):
                if word[k] == word_to_find[k]:
                    print(f"La lettre {word[k]} est bien la {k+1}{'ème' if  k >= 1 else 'ère'}")
                else:
                    if word[k] in word_to_find:
                        print(f"Il y a la lettre {word[k]} dans le mot")
            lifes -= 1

print(f"Le mot était {word_to_find}")


