import random

nbComputer = random.randint(1, 100)
print("Nombre de l'ordi : ", nbComputer)
n = 0

while True:
    print("Entrez un nombre entre 1 et 100")
    nbInput = int(input())
    n += 1
    if nbInput < nbComputer:
        print("Cherchez plus haut")
    elif nbInput > nbComputer:
        print("Cherchez plus bas")
    else:
        print("Vous avez trouvé le bon nombre après", n, "essais")
        break