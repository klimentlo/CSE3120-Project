# c_game_engine.py in Ship, Captain, and Crew (folder)
'''
title: game engine
author: kliment lo
date-created: 2023/10/16
'''
from a_die import Die
from b_player import Player

class Game:
# --- Attributes
    def __init__(self):
        '''
        creates the two player objects and will decide whether or not the game will have modifiers active
        '''
        self.__Player1 = Player()
        self.__Player2 = Player()
        self.__toggleModifier = False
        self.__conditionsMet = False # will be used to see if the NoPreyNoPay conditions were met
        # prints the intro text
        print("""
Welcome to Ship, Captain, and Crew!
The basis of the game is to find as much gold as possible. Whoever reaches 40 gold first wins! In order to do so, you must first find the Ship, then Captain, then Crew. 
Only then, will you be able to locate treasure. Good luck!""")
# --- Setter Methods
    def menu(self):
        '''
        explains the basis of the game and allows user to toggle on modifiers if they want to
        '''

        choice = input("""
1. Start Game
2. Toggle Modifiers
3. Exit
> """)

        if choice.isnumeric():
            choice = int(choice)
        else:
            print("Invalid Input! ")
            return self.menu()
        if choice == 1:
            pass
        elif choice == 2:
            self.toggleModifier() # runs the toggleModifier function
        elif choice == 3:
            exit()
        else:
            print("Invalid Input!")
            return self.menu()

    def toggleModifier(self):
        '''
        allows the players to select if they want to add more dice or turn on additional feature
        return: none
        '''
        print(f"""
Possible Modifiers you woud like to toggle to the game
1. Amount of Die (current: {self.__Player1.displayDieAmount()})
2. Toggle "No prey No pay"  \/ \/ \/
_____________________________________________________________________________________________ 
|Every round, when you find all Ship Captain Crew, instead of saying Y/n to treausre, you get|
|an oppurtunity to double the earnings. If "NPNP" is typed, it will use the remainder of your|
|rolls of that round to try to roll for a second set of Ship Captain Crew. If it is found    | 
|within your remaining rolls, your treasure for that round will double.                      |
----------------------------------------------------------------------------------------------""")
        modifierSelection = input("> ")
        if modifierSelection.isnumeric():
            modifierSelection = int(modifierSelection)
            if modifierSelection > 0 and modifierSelection < 3:
                pass
            else:
                print("Invalid Input! ")
                return self.toggleModifier()
        else:
            print("Invalid Input! ")
            return self.toggleModifier()
        if modifierSelection == 1:
            print("How many dice per roll? ")
            diceAmount = input("> ")
            if diceAmount.isnumeric():
                diceAmount = int(diceAmount)
                if diceAmount > 3:
                    print(f"Amount of Die has successfully been changed to {diceAmount}. ")
                    pass
                else:
                    print("Invalid Amount! Must have at least 4 die!")
                    return self.toggleModifier()
            self.__Player1.changeDiceAmount(diceAmount)
            self.__Player2.changeDiceAmount(diceAmount)
            return self.menu()
        elif modifierSelection == 2:
            if self.__toggleModifier == True:
                self.__toggleModifier = False
                print("Modifier has been toggled off! ")
            else:
                self.__toggleModifier = True
                print("Modifier has been toggled on! ")
            return self.menu()

    def run(self):
        self.__Player1.changeName()
        self.__Player2.changeName()

        while self.__Player1.getGold() < 39 and self.__Player2.getGold() < 39:
            print ("")
            print(f"{self.__Player1.getName()}'s Turn! ")
            pause = input("Press enter to roll! ")
            rolls = 1 # starts off as round 1
            multiplier = 1
            self.__isToggled = False
            while rolls < 4:
                initialGold = self.__Player1.getGold()
                self.__Player1.rollDice() # roll all the dice that's not in hand
                if self.__Player1.checkRolledDice(6, rolls): # checks if any of the rolled dice are 6
                    if self.__Player1.checkRolledDice(5, rolls): # if 6 has already been found, look for 5
                        if self.__Player1.checkRolledDice(4, rolls): # if 5 has already been found, look for 4
                            if self.__isToggled == True: # if they have found ANOTHER set of shipcaptaincrew, then multiplier = 2
                                multiplier = 2
                            decision = self.__Player1.takeTreasure(rolls, self.__toggleModifier, multiplier)  # once found, ask if they want to take treasure. There is also measurements to calcualte if they have any rerolls left. IF not, it automatically adds it to their total
                            if decision == "toggleOn":
                                self.__Player1.resetDice()  # after their rolls are all used up, reset their dice
                                self.__isToggled = True
                            elif decision == True:
                                rolls = 4 # ends their turn
                                self.__Player1.displayGold()
                            elif decision == False:
                                pass
                rolls += 1
            # While loop is broken out once 3 rolls have been done
            if initialGold == self.__Player1.getGold(): # if there is no difference in gold from before and after
                print(f"{self.__Player1.getName()} found no gold! ")
            #Resets the things
            self.__Player1.resetDice() # after their rolls are all used up, reset their dice and hand
            self.__isToggled = False
            if self.__Player1.getGold() >= 40:
                break
            # PLAYER TWO'S TURN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111
            print("")
            print(f"{self.__Player2.getName()}'s Turn! ")
            pause = input("Press enter to roll! ")
            rolls = 1  # starts off as round 1
            multiplier = 1
            while rolls < 4:
                initialGold = self.__Player2.getGold()
                self.__Player2.rollDice()  # roll all the dice that's not in hand
                print(self.__Player2.displayDice())
                if self.__Player2.checkRolledDice(6, rolls):  # checks if any of the rolled dice are 6
                    if self.__Player2.checkRolledDice(5, rolls):  # if 6 has already been found, look for 5
                        if self.__Player2.checkRolledDice(4, rolls):  # if 5 has already been found, look for 4
                            if self.__isToggled == True:  # if they have fund ANOTHER set of shipcaptaincrew, then multiplier = 2
                                multiplier = 2
                            decision = self.__Player2.takeTreasure(rolls, self.__toggleModifier, multiplier)  # once found, ask if they want to take treasure. There is also measurements to calcualte if they have any rerolls left. IF not, it automatically adds it to their total
                            if decision == "toggleOn":
                                self.__Player2.resetDice()  # after their rolls are all used up, reset their dice
                                self.__isToggled = True
                            elif decision == True:
                                rolls = 4  # ends their turn
                                self.__Player2.displayGold()
                            elif decision == False:
                                pass
                rolls += 1
            # While loop is broken out once 3 rolls have been done
            if initialGold == self.__Player2.getGold():  # if there is no difference in gold from before and after
                print(f"{self.__Player2.getName()} found no gold! ")
            self.__Player2.resetDice()  # after their rolls are all used up, reset their dice and hand
            self.__isToggled = False

        if self.__Player1.getGold() >= 40:
            print(f"{self.__Player1.getName()} has won! ")
        else:
            print(f"{self.__Player2.getName()} has won!")
        print("")
        print("Here are the final scores: ")
        print(f"{self.__Player1.getName()}'s total gold: {self.__Player1.getGold()}")
        print(f"{self.__Player2.getName()}'s total gold: {self.__Player2.getGold()}")
        print("Thanks for playing! ")
        print("Returning to main menu... ")


if __name__ == "__main__":
    Game = Game()
    Game.menu()
    Game.run()