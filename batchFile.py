import os

files = os.listdir('./files')
print(files)
for file in files:
    print('******* Traitement du fichier', file, '*******')

    # Lecture et remplacement 
    path = './files/' + file
    f = open(path, 'r') # r pour read
    content = f.read()
    newContent = content.replace('Ryan', 'Abdel')
    f.close()

    # Ecriture
    f = open(path, 'w')
    f.write(newContent)
    f.close()
    print('******* Traitement FINITO *******')