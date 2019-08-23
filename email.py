# a partir d'un fichier txt contenant 10 adresses email séparées par des sauts de ligne, créer un script python qui va parcourir le fichier et ajoute après chaque mail une tab puis un mdp généré de manière aléatoire (longueur 12 caractères, mix de chiffres et de lettres)

import random
import string 

def randomString(stringLength=12):
    format = string.ascii_letters + string.digits
    return ''.join(random.choice(format) for i in range(stringLength))

with open('email-list-new.txt', 'w') as out_file:
    with open('email-list.txt', 'r') as in_file:
        for line in in_file:
            password = randomString()
            out_file.write(line.rstrip('\n') + '\t' + password + '\n') 