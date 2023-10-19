# b_player.py in Ship, Captain, and Crew (folder)
'''
title: player class
author: kliment lo
date-created: 2023/10/16
'''

from a_die import Die

class Player:
    '''
    The player for the game ship captain crew

    :attributes:
    - DICE
    - GOLD

    :behaviors:
    - rollDice()
    - holdDie()
    - addToGold()
    - getGold()
    '''

    def __init__(self):
        '''
        creates a player object
        '''
        self.__NAME = input("Name: ")
        self.__DICE = [Die(), Die(), Die(), Die(), Die(), Die()]
        self.__HELD_DICE = []
        self.__TOTAL_GOLD = 0


    def rollDice(self):
        '''
        rolls all the die in DICE
        :return: none
        '''
        for die in self.__DICE:
            die.rollNum()

    def holdDie(self):
        '''
        user selects die to save
        :return: none
        '''
        print("Select a die to hold ")
        for i in range(len(self.__DICE)):
            print(f"{i+1}. {self.__DICE[i].getNumber()}")
        DIE = int(input("> ")) - 1
        self.__HELD_DICE.append(self.__DICE.pop(DIE))

        print("Dice Remaining")
        for die in self.__DICE:
            print(die.getNumber())

        print("Held Dice: ")
        for die in self.__HELD_DICE:
            print(die.getNumber())

        #ask to gold more dice
        AGAIN = input("Hold More? (y/N)")
        if AGAIN.upper() == "Y":
            return self.__holdDie()


    def addGold(self, GOLD_ADDING):
        '''
        adding new points to the player gold
        :param GOLD_ADDING: int
        :return: none
        '''
        self.__TOTAL_GOLD = self.__TOTAL_GOLD + GOLD_ADDING

    def resetDice(self):
        """
        put all dice back in self.DICE
        :return:
        """
        self.__DICE = [Die(), Die(), Die(), Die(), Die(), Die()]
        self.__HELD_DICE = []

# --- ACCESSORS --- # (outputs)
    def displayDice(self):
        '''
        print all dice in self.DICE
        :return: none
        '''
        for die in self.__DICE:
            print(die.getNumber())

    def displayHeldDice(self):
        '''
        print all dice in self.DICE and self.HELD_DICE
        :return:
        '''
        print("Held Dice:")
        for die in self.__HELD_DICE:
            print(die.getNumber())

    def getGold(self):
        '''
        return the gold to the rest of the program
        :return: int
        '''
        return self.__TOTAL_GOLD

    def getName(self):
        return self.__NAME

    def checkRolledDice(self, WANTEDVALUE):
        for i in range(len(self.__DICE)):
            print(self.__DICE[i].getNumber())
            if self.__DICE[i].getNumber() == WANTEDVALUE: # if the numbers of the dices rolled match the value that we're looking for
                self.__HELD_DICE.append(self.__DICE.pop(i))# append the dice into the hand
                return True
        return False

    def checkHeldDice(self, WANTEDVALUE):
        for i in range(len(self.__HELD_DICE)): # for the amount of held dice
            if WANTEDVALUE == self.__HELD_DICE[i]: # if the value that's being searched for is found in here
                return True # itll stop searching
        return False # if its not found, return false


if __name__ == "__main__":
    Player = Player()
    Player.rollDice()
    print(Player.displayAllDice())