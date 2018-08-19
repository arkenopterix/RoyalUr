from random import *


##############class#####################
class Dice:
    """ This class defines the dice object used in the game"""
##############constructeur##################
    def __init__(self):
        pass

    def roll(self):
        result = randint(0,4)
        return result