import random
import curses
import time

from Direction import Direction
from Maze import Maze


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
    # maze = Maze(height, width, h_walls, v_walls)
    while True:
        # time.sleep(0.25)
        # maze.set_pos(i, j)
        # for line_number, line in enumerate(str(maze).split('\n')):
        #     stdscr.addstr(line_number, 0, line)
        # stdscr.refresh()
        seen.add((i, j))
        cases = possible_cases(height, width, seen, i, j)
        if not cases:
            if not backtrace:
                return Maze(height, width, h_walls, v_walls)
            i, j = backtrace.pop()
            continue
        nb_opening = random.randint(1, len(cases))
        choice = random.choice(cases)
        if choice == Direction.LEFT:
            v_walls[j - 1][i] = False
        elif choice == Direction.RIGHT:
            v_walls[j][i] = False
        elif choice == Direction.UP:
            h_walls[i - 1][j] = False
        elif choice == Direction.DOWN:
            h_walls[i][j] = False
        if nb_opening > 1:
            backtrace.append((i, j))
        i, j = resolve_pos(i, j, choice)


def solve_maze(maze):
    seen = set()
    backtrace = []
    solution = []
    i, j = 0, 0
    while i != maze.height - 1 or j != maze.width - 1:
        maze.set_pos(i, j)
        for line_number, line in enumerate(maze.representation({s: 'O' for s in seen}).split('\n')):
            stdscr.addstr(line_number, 0, line)
        stdscr.refresh()
        time.sleep(0.01)
        seen.add((i, j))
        solution.append((i, j))
        directions = list(filter(lambda x: resolve_pos(i, j, x) not in seen, maze.available_directions(i, j)))
        if not directions:
            if not backtrace:
                return []
            i, j = backtrace.pop()
            solution = solution[:solution.index((i, j))]
            continue
        if len(directions) > 1:
            backtrace.append((i, j))
            choice = random.choice(directions)
        else:
            choice = directions[0]
        (i, j) = resolve_pos(i, j, choice)
    solution.append((maze.height - 1, maze.width - 1))
    maze.set_pos(maze.height - 1, maze.width - 1)
    for line_number, line in enumerate(str(maze).split('\n')):
        stdscr.addstr(line_number, 0, line)
    stdscr.refresh()
    time.sleep(1)
    return solution


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
try:
    maze = random_maze(20, 65)
    solutions = solve_maze(maze)
    maze.unset_pos()
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()
if not solutions:
    print('IMPOSSIBLE')
else:
    print(maze.representation({s:'*' for s in solutions}))
