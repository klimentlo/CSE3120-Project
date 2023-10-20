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
    def run(self):
        while self.__Player1.getGold() < 29 and self.__Player2.getGold() < 29:
            print(f"{self.__Player1.getName()}'s Turn")
            turns = 0
            while turns < 4:
                #for i in range(3): # for the 3 rolls they get per turn
                self.__Player1.rollDice() # roll all the dice that's not in hand
                #print(self.__Player1.displayDice())
                if self.__Player1.checkRolledDice(6): # checks if any of the rolled dice are 6
                    if self.__Player1.checkRolledDice(5):
                        if self.__Player1.checkRolledDice(4):
                            print("Treasure Woohoo Add tmr")
                #print(self.__Player1.displayHeldDice())
                turns += 1
            pause = input("round has ended")


if __name__ == "__main__":
    Game = Game()
    Game.run()