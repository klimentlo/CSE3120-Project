# c_game_engine.py in Ship, Captain, and Crew (folder)
'''
title: game engine
author: kliment lo
date-created: 2023/10/16
'''
from a_die import Die
from b_player import Player

class Game:
    def __init__(self):
        self.__Player1 = Player()
        self.__Player2 = Player()
        self.__toggleModifier = False
    def setup(self):
        '''
        explains the basis of the game and allows user to toggle on modifiers if they want to
        '''
        print("""
Welcome to Ship, Captain, and Crew!
The basis of the game is to find as much gold as possible. Whoever gets at least 30 gold first wins! In order to do so, you must first find the Ship, then Captain, then Crew. Good luck!""")

        choice = input("""
1. Start Game
2. Toggle Modifiers
3. Exit 
> """)

        if choice.isnumeric():
            choice = int(choice)
        else:
            print("Invalid Input! ")
            return self.setup()
        if choice == 1:
            pass

        elif choice == 2:
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
            else:
                print("Invalid Input! ")
                return self.setup()
            if modifierSelection == 1:
                print("How many dice per roll? ")
                diceAmount = input("> ")
                if diceAmount.isnumeric():
                    diceAmount = int(diceAmount)
                self.__Player1.changeDiceAmount(diceAmount)
                self.__Player2.changeDiceAmount(diceAmount)
            elif modifierSelection == 2:
                self.__toggleModifier = True
        elif choice == 3:
            exit()
        else:
            print("Invalid Input!")
            return self.setup()


    def run(self):
        self.__Player1.changeName()
        self.__Player2.changeName()
        while self.__Player1.getGold() < 29 and self.__Player2.getGold() < 29:
            print(f"{self.__Player1.getName()}'s Turn! ")
            rolls = 1 # starts off as round 1
            while rolls < 4:
                initialGold = self.__Player1.getGold()
                self.__Player1.rollDice() # roll all the dice that's not in hand
                print(self.__Player1.displayDice())
                if self.__Player1.checkRolledDice(6, rolls): # checks if any of the rolled dice are 6
                    if self.__Player1.checkRolledDice(5, rolls): # if 6 has already been found, look for 5
                        if self.__Player1.checkRolledDice(4, rolls): # if 5 has already been found, look for 4
                            if self.__Player1.takeTreasure(rolls, self.__toggleModifier): # once found, ask if they want to take treasure. There is also measurements to calcualte if they have any rerolls left. IF not, it automatically adds it to their total
                                rolls = 4 # ends their turn
                                self.__Player1.displayGold()

                rolls += 1
            if initialGold == self.__Player1.getGold(): # if there is no difference in gold from before and after
                print(f"{self.__Player1.getName()} found no gold! ")
            self.__Player1.resetDice() # after their rolls are all used up, reset their dice
                #print(self.__Player1.displayHeldDice())
            pause = input("Their turn as has ended")


if __name__ == "__main__":
    while True:
        Game = Game()
        Game.setup()
        Game.run()