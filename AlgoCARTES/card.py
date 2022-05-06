class Card:
    def __init__(self, name, cost, description):
        self._name= name
        self._cost= cost
        self._description = ""
        
    def getName(self):
        return self._name

    def setName(self, name):
        self._name= name

    def getCost(self):
        return self._cost

    #def setCost(self):
        #return self._cost
    
    def getDescription(self):
        return self._description

class SummonedCard:
    def __init__(self, name, cost, description):
        self._name= name
        self._cost= cost
        self._description = ""
        
    def getName(self):
        return self._name

    def setName(self, name):
        self._name= name

    def getCost(self):
        return self._cost
    
    def getDescription(self):
        return self._description


class Crystal(Card):
    def __init__(self, name, value,cost, description):
        Card.__init__(self, "Cristal",0,"Un cristal")
        self._name = name
        self._value = value
        self._cost = cost
        self._description = description


class Creature(Card):
    def __init__(self, name, value, atk, hp, cost, description):
        Card.__init__(self, name,cost, description)
        self._value= value
        self._atk= atk
        self._hp= hp
        self.cost = cost

    def getAtk(self):
        return self._atk
    


class Blast(Card):
    def __init__(self, name, price, strength, cost, description):
        Card.__init__(self, name, cost, description)
        self._price= price
        self._strength= strength
    
    def getStrength(self):
        return self._strength




