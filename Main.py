import random
from enum import Enum

from Maze import Maze


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


def possible_cases(height, width, seen, i, j):
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


def resolve_pos(i, j, direction):
    return i + direction.value[0], j + direction.value[1]


def random_maze(height, width):
    i, j = 0, 0
    h_walls = [[True] * width for _ in range(height - 1)]
    v_walls = [[True] * height for _ in range(width - 1)]
    seen = set()
    backtrace = []
    while True:
        # print(Maze(height, width, h_walls, v_walls).print_with_post(i,j))
        seen.add((i, j))
        cases = possible_cases(height, width, seen, i, j)
        if not cases:
            if not backtrace:
                return Maze(height, width, h_walls, v_walls)
            i, j = backtrace.pop()
            continue
        nb_opening = random.randint(1, len(cases))
        choices = random.sample(cases, k=nb_opening)
        for choice in choices:
            if choice == Direction.LEFT:
                v_walls[j - 1][i] = False
            elif choice == Direction.RIGHT:
                v_walls[j][i] = False
            elif choice == Direction.UP:
                h_walls[i - 1][j] = False
            elif choice == Direction.DOWN:
                h_walls[i][j] = False
        next_direction = random.choice(choices)
        choices.remove(next_direction)
        for choice in choices:
            backtrace_pos = resolve_pos(i, j, choice)
            seen.add(backtrace_pos)
            backtrace.append(backtrace_pos)
        i, j = resolve_pos(i, j, next_direction)


maze = random_maze(20, 20)
print(maze)
