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
        self.__Modifiers = [None, None]

    def run(self):
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
                            if self.__Player1.takeTreasure(rolls): # once found, ask if they want to take treasure. There is also measurements to calcualte if they have any rerolls left. IF not, it automatically adds it to their total
                                rolls = 4 # ends their turn
                                self.__Player1.displayGold()
                rolls += 1
            if initialGold == self.__Player1.getGold(): # if there is no difference in gold from before and after
                print(f"{self.__Player1.getName()} found no gold! ")
            self.__Player1.resetDice() # after their rolls are all used up, reset their dice
                #print(self.__Player1.displayHeldDice())
            pause = input("Their turn as has ended")

def menu():
    '''
    explains the basis of the game and allows user to toggle on modifiers if they want to
    '''
    print("""
Welcome to Ship, Captain, and Crew!
The basis of the game is to find as much gold as possible. Whoever gets at least 30 gold first wins! In order to do so, you must first find the Ship, then Captain, then Crew. Good luck!
""")

    choice = input("""
1. Begin Game
2. Toggle Modifiers
3. Exit """)

if __name__ == "__main__":
    while True:
        modifiers = menu()
        Game = Game()
        Game.run()