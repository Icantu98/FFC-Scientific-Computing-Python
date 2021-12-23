class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')
    
    def party(self):
        self.x = self.x +1
        print('So Far', self.x)
    
    #def __del__(self):
    #    print('I am destructed', self.x) # will tell us when its destructed 

#Making a SubClass
class FootballFan(PartyAnimal):
    points = 0
    #inherits all the methods you made in the PartyAnimal Class
    def touchdown(self):
        self.points = self.points +7
        self.party()
        print(self.name,'Points',self.points)


PartyAnimal('').party()

# how to compress it
an = PartyAnimal('')
# Acts the same as PartyAnimal().party()
an.party()
an.party()
an.party()

# reassigning the variable destructs the party() object
an = 42

s = PartyAnimal('Sally')
s.party() 

j = FootballFan('Jim')

j.touchdown() #has access to PartyAnimal Class
s.party()   


