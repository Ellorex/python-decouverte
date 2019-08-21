import operator

students = [
    {"name": "Laurence", "average": 15},
    {"name": "Jessy", "average": 12},
    {"name": "Paul", "average": 19},
    {"name": "Abdelito", "average": 17}
]

def getBest(entry):
    best = entry[0]
    worst = entry[0]
    for e in entry[1:]:
        if e["average"] > best["average"]:
            best = e
        if e["average"] < worst["average"]:
            worst = e
    print("best :", best)
    print("worst :", worst)

getBest(students)