import curses
import time

from DFSMazeGenerator import DFSMazeGenerator
from DFSMazeSolver import DFSMazeSolver


def display_maze(maze, cells):
    time.sleep(0.5)
    for line_number, line in enumerate(maze.representation(cells).split('\n')):
        stdscr.addstr(line_number, 0, line)
    stdscr.refresh()


# maze = DFSMazeGenerator(display_maze).generate(5, 5)
# solutions = DFSMazeSolver(display_maze).solve(maze)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
try:
    maze = DFSMazeGenerator(lambda *args: None).generate(10, 10)
    solutions = DFSMazeSolver(display_maze).solve(maze)
    maze.unset_pos()
finally:
    curses.echo()
    curses.nocbreak()
    curses.endwin()
if not solutions:
    print('IMPOSSIBLE')
else:
    print(maze.representation({s: '*' for s in solutions}))
