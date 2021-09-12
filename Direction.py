from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    def resolve_pos(self, i, j):
        return i + self.value[0], j + self.value[1]
