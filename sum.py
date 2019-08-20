print("Entrer un nombre")
entry = int(input())
sumNb = 0

while entry != 0:
    sumNb += entry
    print("Entrer un nombre")
    entry = int(input())
    if entry == 0:
        print("La somme vaut", sumNb)
