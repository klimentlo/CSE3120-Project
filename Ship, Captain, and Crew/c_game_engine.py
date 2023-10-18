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
        print(self.__Player1)
        while self.__Player1.getGold() < 29 and self.__Player2.getGold() < 29:
            print(f"{self.__Player1.getName()}'s Turn")



if __name__ == "__main__":
    Game = Game()
    print(Game)
    Game.run()