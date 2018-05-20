import logging


class Cell:
    def __init__(self, x, y):
        self.alive = False
        self.next_status = None
        self.x = x
        self.y = y

    def toggle_status(self):
        self.alive = not self.alive

    def count_alive_neigbhours(self, cells):
        """
        Counts alive neighbours.
        :param cells: list of cells available in grid
        :return: int
        """
        #@ TODO: add variable that will represent amount of live neighbours
        # check Moore's neighbourhood (8 neighbours)
        # which are the cells that are horizontally,
        # vertically or diagonally adjacent
        #@ TODO: loop over neighbourhood
        # don't check ourself
        #@ TODO: check the state of a neighbour - if it's alive add it
        pass

    def apply_conway_rules(self, cells):
        """
        Verify amount of alive neighbours against Conways rule.
        :param cells: list of cells available in grid
        :return: True or False (cell lives or dies)
        """
        #@ TODO: check Conway's rules
        pass