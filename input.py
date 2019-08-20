print("Combien d'étudiants au maximum sont attendus ?")
nbStudentsMax = input()
print("Votre réponse est",nbStudentsMax,"étudiants max")

print("Combien y a-t-il d'étudiants présents ?")
nbStudentsAttending = input()

if int(nbStudentsAttending) > int(nbStudentsMax) / 2:
    print("Le cours aura bien lieu")
else:
    print("Il n'y a pas assez d'étudiants")