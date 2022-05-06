from card import Card


class Mage:
     def __init__(self,name,hp,currentMana,maxMana,description):
        self._name = name
        self._hp = hp
        self._currentMana = currentMana
        self._maxMana = maxMana

     def getName(self):
        return self._name

     def getHp(self):
        return self._hp

     def get(self):
        return self._hp

     def getMana(self):
        return self._currentMana

     def setMana(self, value):
        
        self._currentMana -= value
        return self._currentMana

     def setHp(self, strength):
        
        self._hp -= strength
        return self._hp

     def resetMana(self):
        self._currentMana = self._maxMana
         
        return self._currentMana

        
        
   

   