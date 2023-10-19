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
            for i in range(3): # for the 3 rolls they get per turn
                self.__Player1.rollDice() # roll all the dice that's not in hand
                if self.__Player1.checkHeldDice(6) == False: # if the desired dice isn't already in the hand
                    if self.__Player1.checkRolledDice(6) == True: # then checks if the desired dice is on the table
                        pause = input(f" Currently Held Dice Below: {self.__Player1.displayHeldDice()}")
                        pass # if so, its automatically appended into held dice if its found here
                    else:
                        # if it is not found
                        break
                if self.__Player1.checkHeldDice(5) == False:
                    if self.__Player1.checkRolledDice(5) == True:
                        pass
                if self.__Player1.checkHeldDice(4) == False:
                    if self.__Player1.checkRolledDice(4) == True:
                        pass



if __name__ == "__main__":
    Game = Game()
    Game.run()