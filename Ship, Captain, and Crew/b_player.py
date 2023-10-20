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
        # first checks if its already held or not
        for i in range(len(self.__HELD_DICE)):  # then for the length of held dice
            if self.__HELD_DICE[i].getNumber() == WANTEDVALUE:  # if the value we want is already in our hand, dont do anything and go back
                return True  # already found

        for i in range(len(self.__DICE)-1, -1, -1): # for the length of rolled dice
            if self.__DICE[i].getNumber() == WANTEDVALUE: # check to see if any of the numbers are what we are looking for
                self.__HELD_DICE.append(self.__DICE.pop(i))  #if it runs through the entire hand and doesn't find a match, it will append it into the thing.
                return True

if __name__ == "__main__":
    Player = Player()
    Player.rollDice()
    print(Player.displayAllDice())