'''
Dans le dossier /nodanger, créer un sous dossier /log et y ranger les fichiers .log. Pareil pour les fichiers en png.
Les fichiers en .txt sont eux supprimés.
'''


import os 
import datetime

files = os.listdir('./nodanger')
datenow = datetime.datetime.now()
datenowFormatted = datenow.strftime('%d-%m-%Y %H-%M-%S')
print(datenowFormatted)


def clean(files):
    # Ouverture d'un fichier de log
    log = open('clean.log', 'a') # a comme append, contrairement au 'w' qui écrase
    for file in files:
        if file.endswith('.png'):
            if os.path.exists("./nodanger/png"):
                os.rename("./nodanger/"+file, "./nodanger/png/" + file)
            else:
                os.makedirs("./nodanger/png")
                os.rename("./nodanger/"+file, "./nodanger/png/" + file)
        elif file.endswith('.log'):
            if os.path.exists("./nodanger/log"):
                os.rename("./nodanger/"+file, "./nodanger/log/" + file)
            else:
                os.makedirs("./nodanger/log")
                os.rename("./nodanger/"+file, "./nodanger/log/" + file)
        elif file.endswith('.txt'):
            print(file)
            if os.path.exists("./nodanger/"+file):
                absPath = os.path.abspath('./nodanger/' + file)
                log.write(datenowFormatted + '\t' + absPath + '\t' + 'deleted \n')
                os.remove("./nodanger/"+file)
    log.close()
clean(files)