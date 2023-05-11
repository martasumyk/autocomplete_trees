'''
Main module to create rabbits and their logic of game.
'''
import random

class Rabbit:
    '''
    Class to create rabbits.
    '''
    def __init__(self, energy=random.randint(1, 10), sense=random.randint(1, 5)):
        '''
        Initializing the rabbit`s data.
        '''
        self.energy = energy
        self.sense = sense

    def eat(self):
        '''
        Method that helps rabbit to eat.
        '''
        self.energy += 5

    def run(self):
        '''
        Method that helps rabbit to run.
        '''
        raise NotImplementedError

    def crossing(self, other):
        '''
        Method to cross two rabbits.
        '''
        new_rabbit = Rabbit()


class Food:
    '''
    Class to create food for rabbits.
    '''
    def __init__(self, coordinates):
        '''
        Initializes the food with it`s coordinates.
        '''
        self.coordinates = coordinates



# board = Board(3, 3)
# print(board.distance((1, 2), (2, 3)))
# example of 3*3 game board:
# [[0, 0, rabbit], [eat, rabbit, 0], [0, 0, eat]]

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
