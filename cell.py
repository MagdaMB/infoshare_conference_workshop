import logging


class Cell:
    def __init__(self, x, y):
        self.alive = False
        self.next_status = None
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Cell({self.x}, {self.y}'

    def toggle_status(self):
        self.alive = not self.alive

    def change_status(self, cells):
        """
        Counts alive neighbours and based on that applies Conways rule
        :param cells: list of cells available in grid
        :return: True or False (cell lives or dies)
        """
        num_alive = 0
        # check Moore's neighbourhood (8 neighbours)
        # which are the cells that are horizontally,
        # vertically or diagonally adjacent
        for i in (self.x - 1, self.x, self.x + 1):
            for j in (self.y - 1, self.y, self.y + 1):
                # don't check ourself
                if i == self.x and j == self.y:
                    continue
                try:
                    if cells[i][j].alive:
                        num_alive += 1
                except IndexError:
                    logging.log(
                        logging.WARNING,
                        f'{self} doesn\'t have neighbour at x:{i} y:{j}'
                    )

        if self.alive:
            return not (num_alive == 2 or num_alive == 3)
        else:
            return num_alive == 3
