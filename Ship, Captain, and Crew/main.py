# main.py in Ship, Captain, Crew (folder)
'''
title: main program thingy
author: kliment lo
date-created: 2023/10/20
'''

class Main:
    from c_game_engine import Game

    def __init__(self):
        while True:
            self.__GAME = Main.Game()
            self.__GAME.menu()
            self.__GAME.run()

if __name__ == "__main__":
    Main()