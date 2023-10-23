# b_player.py in Ship, Captain, and Crew (folder)
'''
title: player class
author: kliment lo
date-created: 2023/10/16
'''

from a_die import Die

Unit = {
    6 : "Ship",
    5 : "Captain",
    4 : "Crew",
}

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
        self.__NAME = ""
        self.__DICE = [Die(), Die(), Die(), Die(), Die()]
        self.__DICE_AMOUNT = 5
        self.__HELD_DICE = []
        self.__TOTAL_GOLD = 0

    def changeName(self):
        '''
        assigns name to players
        '''
        self.__NAME = input("Name: ")

    def rollDice(self):
        '''
        rolls all the die in DICE
        :return: none
        '''
        for die in self.__DICE:
            die.rollNum()



    def changeDiceAmount(self, DICEAMOUNT):
        '''
        before game, can choose how many dice is used per roll
        '''
        self.__DICE_AMOUNT = DICEAMOUNT # saves into variable
        self.__DICE = [] # resets dice amount
        for i in range(self.__DICE_AMOUNT): # for amount of desired dice
            self.__DICE.append(Die()) # make that many

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
        self.__DICE = [] # makes dice dead
        for i in range(self.__DICE_AMOUNT): # for the amount of dice wante d
            self.__DICE.append(Die()) # make that many

        self.__HELD_DICE = [] # reset hand

    def checkRolledDice(self, WANTEDVALUE, TURN):
        '''
        Chekcs if the dice matches our wanted value, appended our desired things in order into the hand
        '''
        # first checks if its already held or not
        for i in range(len(self.__HELD_DICE)):  # then for the length of held dice
            if self.__HELD_DICE[i].getNumber() == WANTEDVALUE:  # if the value we want is already in our hand, dont do anything and go back
                return True  # already found

        for i in range(len(self.__DICE)-1, -1, -1): # for the length of rolled dice
            if self.__DICE[i].getNumber() == WANTEDVALUE: # check to see if any of the numbers are what we are looking for
                print(f"{Unit[WANTEDVALUE]} has been found! (Roll {TURN})")
                self.__HELD_DICE.append(self.__DICE.pop(i))  #if it runs through the entire hand and doesn't find a match, it will append it into the thing.
                return True

    def takeTreasure(self, ROLLS, TOGGLEMODIFIER, MULTIPLIER):
        '''
        Calculates and tells user how much treasure they have from that roll
        '''


        treasure = 0
        rerolls = 3 - ROLLS
        for die in self.__DICE:
            treasure += die.getNumber()

        if ROLLS == 3: # if they have no rerolls left
            print(f"You found {treasure * MULTIPLIER} pieces of gold! ") # just tell them how much they found
            self.__TOTAL_GOLD += (treasure * MULTIPLIER) # add the treasure
            return True

        print(f"You currently found {treasure * MULTIPLIER} pieces of gold! Keep Treasure? (Y/n) (Rerolls left: {rerolls})")
        takeGold = input("> ")
        # This section is if the double or nothing option is selected
        if TOGGLEMODIFIER == True:
            if takeGold == "NPNP":
                print("Player has participated in No Prey No Pay! ")
                return "toggleOn"
        if takeGold == "Y" or takeGold == "y":
            self.__TOTAL_GOLD += (treasure * MULTIPLIER)
            return True
        else: # if they type anything aside from Y or y, then dont add gold
            return False

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

    def displayDieAmount(self):
        '''
        prints the amount of dice there is in the game as of right now
        '''
        return len(self.__DICE)

    def displayGold(self):
        '''
        prints out the gold they just got and how much they have currently
        '''
        print(f"{self.__NAME} has a total of {self.__TOTAL_GOLD} Gold! ")

    def getGold(self):
        '''
        return the gold to the rest of the program
        :return: int
        '''
        return self.__TOTAL_GOLD

    def getName(self):
        return self.__NAME



if __name__ == "__main__":
    Player = Player()
    Player.rollDice()
    print(Player.displayAllDice())