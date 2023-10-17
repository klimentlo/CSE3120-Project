# a_die.py in Ship, Captain, and Crew (folder)
'''
title: die class
author: kliment lo
date-created: 2023/10/16
'''
class Die:
    '''
    Create a die to roll for random numbers

    :attributes:
    - DIE_MAX_NUMBER
    - DIE_NUMBER

    :methods:
    - rollNum()
    - getNum()
    '''

    from random import randint

    def __init__(self):
        '''
        constructs the die object
        '''
        self.__DIE_MAX_NUMBER = 6
        self.__DIE_NUMBER = None

    def rollNum(self):
        '''
        updates DIE_NUMBER with a new number
        :return: None
        '''
        self.__DIE_NUMBER = Die.randint(1, self.__DIE_MAX_NUMBER)

    def getNumber(self):
        '''
        returns the number the dice rolled
        :return: (int)
        '''
        return self.__DIE_NUMBER
if __name__ == "__main__":
    Die = Die()