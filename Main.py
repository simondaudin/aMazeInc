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


def display_maze(maze, cells):
    time.sleep(0.05)
    for line_number, line in enumerate(maze.representation(cells).split('\n')):
        stdscr.addstr(line_number, 0, line)
    stdscr.refresh()


def random_maze(height, width):
    i, j = 0, 0
    h_walls = [[True] * width for _ in range(height - 1)]
    v_walls = [[True] * height for _ in range(width - 1)]
    seen = set()
    backtrace = []
    maze = Maze(height, width, h_walls, v_walls)
    while True:
        maze.set_pos(i, j)
        display_maze(maze, {})
        seen.add((i, j))
        backtrace.append((i, j))
        cases = possible_cases(height, width, seen, i, j)
        if not cases:
            return_to = None
            for p_i, p_j in backtrace[::-1]:
                is_there_neighbors = possible_cases(height, width, seen, p_i, p_j)
                if is_there_neighbors:
                    return_to = (p_i, p_j)
                    break
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
        i, j = resolve_pos(i, j, choice)


def solve_maze(maze):
    seen = set()
    backtrace = []
    solution = []
    i, j = 0, 0
    while i != maze.height - 1 or j != maze.width - 1:
        maze.set_pos(i, j)
        display_maze(maze, {s: 'O' for s in seen})
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
    display_maze(maze, {s: 'O' for s in seen})
    return solution



stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
try:
    maze = random_maze(10, 10)
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
