isStrong = True
nbStudents = 5
nbStudentsMax = 16

if isStrong:
    print('il est fooooort')

if nbStudents >= nbStudentsMax:
    print('Y a plus de place')
else: 
    nbMissing = nbStudentsMax - nbStudents
    print('Il manque ', nbMissing, ' etudiants pour que le groupe soit complet')
    if nbMissing < 8:
        print('Quorum atteint')
    else:
        print('Blocage électoral ', nbMissing, ' étudiants manquants')