template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Webpage</title>
</head>
<body>
    <h1>[firstname] [lastname]</h1>
    <p>Moyenne: [average]</p>
    <img src="[imgSrc]" width="400">
</body>
</html>
'''



student1 = { "firstname": "Abdelwaheb", "lastname": "Messaouidi", "country": "Algérie", "notes":[4,15,17]}
student2 = { "firstname": "Paolo", "lastname": "Del Priore", "country": "Pologne", "notes":[13,12,14]}
student3 = { "firstname": "Christophe", "lastname": "Dufour", "country": "Italie", "notes":[3,4,2]}
students = [student1, student2, student3]

def getAverage(grades):
    grade = 0
    for g in grades:
        grade = grade + g
    average = grade / len(s["notes"])
    return average

for s in students:
    studAve = getAverage(s["notes"])
    # à chaque passage dans la boucle, on génère un fichier
    filename = "webpage_" + s["firstname"].lower() + '.html'
    imgpath = '../flags/' + s["country"].lower() + '.png'
    f = open('./webpages/' + filename, 'w') # le 'w' autorise l'écriture ("writeable)"
    newTemplate = template.replace('[firstname]', s["firstname"]).replace('[lastname]', s["lastname"]).replace("[average]", str(studAve)).replace('[imgSrc]', imgpath)
    f.write(newTemplate)
    f.close()

