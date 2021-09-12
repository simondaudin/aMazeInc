import random

from Direction import Direction
from Maze import Maze
from MazeGenerator import MazeGenerator


class DFSMazeGenerator(MazeGenerator):

    def __init__(self, display_maze):
        self.display_maze = display_maze

    @staticmethod
    def possible_next_cells(height, width, seen, i, j):
        res = []
        if i > 0:
            res.append(Direction.UP)
        if i < height - 1:
            res.append(Direction.DOWN)
        if j > 0:
            res.append(Direction.LEFT)
        if j < width - 1:
            res.append(Direction.RIGHT)
        return list(filter(lambda x: (i + x.value[0], j + x.value[1]) not in seen, res))

    def generate(self, height, width):
        i, j = 0, 0
        h_walls = [[True] * width for _ in range(height - 1)]
        v_walls = [[True] * height for _ in range(width - 1)]
        seen = set()
        backtrace = []
        maze = Maze(height, width, h_walls, v_walls)
        while True:
            maze.set_pos(i, j)
            self.display_maze(maze, {})
            seen.add((i, j))
            backtrace.append((i, j))
            cases = self.possible_next_cells(height, width, seen, i, j)
            if not cases:
                return_to = next(((p_i, p_j) for p_i, p_j in backtrace[::-1] if
                                  self.possible_next_cells(height, width, seen, p_i, p_j)), None)
                if return_to:
                    backtrace = backtrace[:backtrace.index(return_to)]
                    i, j = return_to
                    continue
                else:
                    return Maze(height, width, h_walls, v_walls)
            choice = random.choice(cases)
            if choice == Direction.LEFT:
                v_walls[j - 1][i] = False
            elif choice == Direction.RIGHT:
                v_walls[j][i] = False
            elif choice == Direction.UP:
                h_walls[i - 1][j] = False
            elif choice == Direction.DOWN:
                h_walls[i][j] = False
            i, j = choice.resolve_pos(i, j)
