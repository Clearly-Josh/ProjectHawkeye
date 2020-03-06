from Names import names
from random import randint
import json
Corpses = 0
Clones = []
def Cloning(AmountofClones, Generations):
    #strength25,intelligence50,charisma35
    #Gunner wrote this
    def Nameslol(argument): #Customized Names
        switcher = {
            'Samuel Aden': [16,25,100,100],
            'Tyler Whiting': [17,100,69,100],
            'Elon Musk': [48,100,5000,100],
            'Gunnar Fecht': [15, 25, 25, 100],
            'Bryson Pfeifer': [15, 25, 70, 70],
            'Sans': [0,900,900,900],
            'Mr. Clark': [27, 500, 500, 500],
            'Yuki Yana': [14, 50, 50, 50],
            'Alana': [16, 80, 80, 100],
            'Emma Pete.': [15, 26, 100, 60],
            'Undyne': [24, 100, 50, 45],
            'Maddie Bogus': [15, 100, 60, 80]
        }
        return switcher.get(argument, [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 1)])
    #Bryson wrote this
    class clone:  #Each individual Clone (Stored in an array)
        def __init__(self):
            #0 = boy
            #1 = girl
            self.partner = {
                'Name': 'single',
                'Strength': 0,
                'Intelligence': 0,
                'Charisma': 0
            }
            self.single = True
            self.sex = randint(0, 1)
            self.name = names[self.sex][randint(0, len(names[self.sex]) - 1)][0]
            x = Nameslol(self.name)
            self.age = x[0]
            self.strength = x[1]
            self.intelligence = x[2]
            self.charisma = x[3]
        def printall(self):
            print(self.name,': ', self.age, self.strength, self.intelligence, self.charisma, self.sex, self.partner['Name'])
        def death(self): #If a clone is below a certain amount they have a chance to die.
            if self.strength <= 25:
                random = randint(1,100)
                strengthdeathpercent = 100 * (self.strength / 25)
                if random >= strengthdeathpercent:
                    return True
            if self.charisma <= 35:
                random = randint(1,100)
                charismadeathpercent = 100 * (self.charisma / 35)
                if random >= charismadeathpercent:
                    return True
            if self.intelligence <= 50:
                random = randint(1,100)
                intelligencedeathpercent = 100 * (self.intelligence / 50)
                if random >= intelligencedeathpercent:
                    return True
            return False
    #Kurt wrote this
    def checkfordeath(): #Function that uses a function to see if clones should be dead
        delete = 0
        global Corpses
        for i in range(len(Clones)):
            if Clones[i - delete].death():
                del Clones[i - delete]
                delete += 1
                Corpses += 1
    def dating(clone, clone1):  #Assigns one partner to another
        clone1.partner['Name'] = clone.name
        clone1.partner['Strength'] = clone.strength
        clone1.partner['Intelligence'] = clone.intelligence
        clone1.partner['Charisma'] = clone.charisma
        clone1.single = False
    for i in range(AmountofClones):
        Clones.append(clone())
    checkfordeath()
    for i in range(Generations):
        for i in range(len(Clones)-1):
            #Looks for a partner
            if Clones[i].single == True:
                partner = randint(0, len(Clones) - 1)
                if Clones[partner].sex != Clones[i].sex and Clones[partner].single == True:
                    dating(Clones[partner], Clones[i])
                    dating(Clones[i], Clones[partner])
            else:
                #Females have a 50% chance to have a kid
                if Clones[i].sex == 1:
                    pergenant = randint(1, 2)
                    if pergenant == 1:
                        kid = clone()
                        kid.intelligence = int(kid.intelligence / 20) + int((Clones[i].intelligence + Clones[i].partner['Intelligence']) / 2)
                        kid.strength = int(kid.strength / 20) + int((Clones[i].strength + Clones[i].partner['Strength']) / 2)
                        kid.charisma = int(kid.charisma / 20) + int((Clones[i].charisma + Clones[i].partner['Charisma']) / 2)
                        Clones.append(kid)
            #As people age they get weaker
            Clones[i].strength += randint(-Clones[i].age, randint(40,70))
            Clones[i].intelligence += randint(-Clones[i].age, randint(40,70))
            Clones[i].charisma += randint(-Clones[i].age, randint(40,70))
            Clones[i].age += randint(7,10)
        checkfordeath()
        for i in range(len(Clones)-1):
            Clones[i].printall()
        input("Continue?: ")
    while 1: #Donno what to say, just spits out mumbo jumbo data
        x = input("Would you like to find anyone?: ")
        if x == 'no':
            break
        Count = 0
        for i in range(len(Clones)-1):
            if x == Clones[i].name:
                Count += 1
                print(Count, '.')
                print('Dating: ',Clones[i].partner['Name'])
                print('--Stength:', Clones[i].partner['Strength'])
                print('--Charisma:', Clones[i].partner['Charisma'])
                print('--Intelligence:', Clones[i].partner['Intelligence'])
                print('Strength: ', Clones[i].strength)
                print('Intelligence: ', Clones[i].intelligence)
                print('Charisma: ', Clones[i].charisma)
                print('Age: ', Clones[i].age)
    print('Amount of Clones: ', len(Clones))
    print('Amount of Corpses', Corpses)
    print('Amount of Corpses and Clones',len(Clones)+Corpses)
    y = []
    for i in range(len(Clones)):
        x = {
            'Strength': Clones[i].strength,
            'Intelligence': Clones[i].intelligence,
            'Charisma': Clones[i].charisma,
			'Name': Clones[i].name
        }
        y.append(x)
    z = json.dumps(y)#Puts it all in a dictionary then into Json
    return z#Spits out the json file.
