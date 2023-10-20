# main.py in Ship, Captain, Crew (folder)
'''
title: main program thingy
author: kliment lo
date-created: 2023/10/20
'''

class Main:
    from c_game_engine import Game

    def __init__(self):
        self.__GAME = Main.Game()
        self.__GAME.run()