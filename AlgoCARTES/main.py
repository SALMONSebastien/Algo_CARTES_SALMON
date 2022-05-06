from secrets import choice
from mage import Mage
from card import Card, Crystal, Creature, Blast

turn = "player"
nbTurn = 1

gameOver = False


card1 = Creature("Golem de feu", 5, 10, 6, 5, "Un golem méchant, et en feu.")
card2 = Creature("Lutin de glace",2, 3, 2, 2, "Un lutin bizarre qui n'a pas froid aux yeux.")
card3 = Blast("BOUM",5,6,5,"Tout est dans le titre.")
card4 = Crystal("Cristal Quelconque", 2,2,"Joli caillou")
card5 = Creature("Dragon Blanc aux Yeux Bleus",8,6,10,8,"Toute référence avec une quelconque carte Yu-Gi-Oh serait purement fortuite")



graveyard = []


yourMage = Mage(input("Bonjour Mage, quel est votre nom ?"),10,8,8,"C'est un mage")
ennemiMage = Mage("Jean-François",10, 8, 8, "C'est Jean-François, le fameux mage noir. Son nom fait peur.")

while (not gameOver):
    if (turn == "player"):
        

        print("Vous avez ", yourMage.getMana(), "pts de Mana. Dans votre main, vous avez : un", card1.getName(),  ", un " + card2.getName(), ", un ", card3.getName(), "et une carte ", card4.getName())
        print()
        print("Que faîtes-vous ?")
        actionChoice = int(input("Invoquer une carte (1) ou attaquer avec une créature? (2) ou mettre fin au tour (0)"))

        if(actionChoice == 1) :

            choiceCard = int(input("Quelle carte jouer ? (de 1 à 4). (0 pour finir le tour)"))

            if (choiceCard == 0):
                
                turn = "enemy"
                yourMage.resetMana()
            

            elif (choiceCard == 1):
                yourMage.setMana(card1.getCost())
                print("Vous invoquez un ", card1.getName(), ". Il crie 'Grou grou'. Il vous reste ", yourMage.getMana(), "pts de Mana. Que faites vous (0 pour fin de tour)") 
                summonedCard = card1.getName()
                turn = "enemy"

            elif (choiceCard == 2):
                yourMage.setMana(card2.getCost())
                print("Vous invoquez un ", card2.getName(), ". Il vous regarde bêtement. Il vous reste ", yourMage.getMana(), "pts de Mana. Que faites vous (0 pour fin de tour)") 
                turn = "enemy"

            elif (choiceCard == 3):
                yourMage.setMana(card3.getCost())
                print("Vous utilisez la carte", card3.getName(), ". Vous infligez ", card3.getStrength(), " à Jean-François.")
                ennemiMage.setHp(5)
                print("Il reste", ennemiMage.getHp(), " à Jean-François.")
                turn = "enemy"



            elif (choiceCard == 4):
                print("Vous utilisez un cristal quelconque. Votre mana a augmenté de 1.")
                yourMage.setMana(-1)

        #if (actionChoice == 2):
            #if (summonedCard == card1.getName()):
                #card1.getName(), " attaque Jean François!", ennemiMage.setHp(card1.getAtk()), ". Il reste à J-F", ennemiMage.getHp(), "pts de vie."



        elif (actionChoice == 0):

            turn = "enemy"
            yourMage.resetMana()

            
    elif(turn == "enemy"):

        print ("Tour ennemi. ", ennemiMage.getName(), "a ", ennemiMage.getHp(), "points de vie. Et il est énervé.")
        print ("JF invoque un ", card5.getName(), "et celui-ci vous attaque et vous inflige", card5.getAtk())
        yourMage.setHp(6)
        print ("Il vous reste",yourMage.getHp(), "points de vie")
        turn = "player"


            
    
