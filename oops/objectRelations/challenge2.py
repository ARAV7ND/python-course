class School:
    def __init__(self,name):
        self.teams = []
        self.name =name
    def addTeam(self,team):
        self.teams.append(team)
    def getTotalPlayersInSchool(self):
        return sum([i.getNumberOfPlayers() for i in self.teams])

class Team:
    def __init__(self,name):
        self.players=[]
        self.name = name
    def addPlayers(self,player):
        self.players.append(player)
    def getNumberOfPlayers(self):
        return len(self.players)

class Player:
    def __init__(self,id,teamName,name):
        self.id = id
        self.teamName = teamName
        self.name = name
p1 = Player(1,'RED','HARRIS')
p2 = Player(1,'RED','CAROL')
p3 = Player(1,'BLUE','JOHNNY')
p4 = Player(1,'BLUE','SARAH')

t1 = Team('RED')
t2 = Team('BLUE')
t1.addPlayers(p1)
t1.addPlayers(p2)
t2.addPlayers(p3)
t2.addPlayers(p4)
school = School('DPS')
school.addTeam(t1)
school.addTeam(t2)
print('total:',school.getTotalPlayersInSchool());