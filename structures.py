students = ['Léa', 'Abdel', 'Jessy', 'Marcel']
print(type(students))

for student in students:
    print(student)

print(len(students))

print(students[1])

students.append('Paolo')

students[2] = "Jessy le boloss"

mon_tuple = ()
print(type(mon_tuple))
coords = (45.85, 78.23)
# Le tuple peut recevoir des données en entrée mais ne peut pas être mis à jour ni recevoir des valeurs supplémentaires

latitude, longitude = 67.32, 88.78
print("type latitude")
print(type(latitude))

# Dictionary
recipe = {'name': 'Tiramisù', 'chef': 'Abdel', 'stars': 5}
recipe["opponent"] = "Laurence" #ajout
recipe["stars"] = 4 #mis à jour
print(recipe)

print('name' in recipe)

# itération sur les clés
for k in recipe.keys():
    print(k)

for v in recipe.values():
    print(v)

for k, v in recipe.items():
    print(k, "=>",v)

# fusion entre dictionnaires
d1 = {"name": "gorgonzola"}
d2 = {"calories": 4574}
d1.update(d2) #d1 étendu avec d2