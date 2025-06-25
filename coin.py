import random

class Coin:
    def __init__(self):

        self.__amount = 20
        self.__sideup = 'Heads'

    def toss(self):

        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

    def get_amount(self):
        return self.__amount

    def set_amount(self, value: int):
        self.__amount += value
        if self.__amount < 0:
            self.__amount = 0