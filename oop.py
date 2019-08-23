class Team:
    # Propriétés toujours publiques en python
    name=''
    stadium=''
    coach=''
    points=0

    # Méthodes
    # la présence de "self" est impérative en premier argument de chaque fonction
    def __init__(self, name): #constructeur
        self.name = name

    def getName(self):
        return self.name
    def win(self):
        self.points += 3
    def draw(self):
        self.points += 1
    def printPoints(self):
        print(self.name + ': ' + str(self.points) + ' points')
        
team1 = Team('Juventus') # pas besoin du mot clé "new" pour créer un objet
team2 = Team('Charenton FC')
team1.win()
team1.win()
team2.draw()
team1.printPoints()
team2.printPoints()