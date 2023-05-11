''' Board '''
class Board:
    '''
    Class to create board.
    '''
    def __init__(self, rows, columns):
        '''
        Initializes the game board.
        '''
        self.board = []

        for _ in range(rows):
            self.board.append([[0] * columns])


    def distance(self, coords1: tuple, coords2: tuple) -> float:
        '''
        Counts distance between two objects on the field by Manhattan metric.
        >>> board = Board(3, 3)
        >>> board.distance((1, 2), (3, 2))
        2
        '''
        return abs(coords2[0] - coords1[0]) + abs(coords2[1] - coords1[1])
