import random

from Direction import Direction


class DFSMazeSolver(object):
    ordered_directions = [Direction.UP, Direction.LEFT, Direction.DOWN, Direction.RIGHT]

    def __init__(self, display_maze):
        self.display_maze = display_maze

    def solve(self, maze):
        seen = set()
        backtrace = []
        solution = []
        i, j = 0, 0
        while i != maze.height - 1 or j != maze.width - 1:
            maze.set_pos(i, j)
            self.display_maze(maze, {s: 'O' for s in seen})
            seen.add((i, j))
            solution.append((i, j))
            directions = list(filter(lambda x: x.resolve_pos(i, j) not in seen, maze.available_directions(i, j)))
            # directions.sort(key=self.ordered_directions.index)
            if not directions:
                if not backtrace:
                    return []
                i, j = backtrace.pop()
                solution = solution[:solution.index((i, j))]
                continue
            if len(directions) > 1:
                for k in range(1, 4):
                    idx = (self.ordered_directions.index(choice if choice else Direction.DOWN) + 2 + k) % 4
                    if self.ordered_directions[idx] in directions:
                        choice = self.ordered_directions[idx]
                        break
                backtrace.append((i, j))
                # choice = random.choice(directions)
            else:
                choice = directions[0]
            (i, j) = choice.resolve_pos(i, j)
        solution.append((maze.height - 1, maze.width - 1))
        maze.set_pos(maze.height - 1, maze.width - 1)
        self.display_maze(maze, {s: 'O' for s in seen})
        return solution
