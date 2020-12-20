class Maze:

    def __init__(self, height, width, h_walls, v_walls):
        self.height = height
        self.width = width
        self.h_walls = h_walls
        self.v_walls = v_walls

    def __repr__(self):
        s = '+' + (Maze.wall_char(True, True)+'+') * self.width + '\n'
        for i in range(self.height - 1):
            s += '|' + ''.join(['  '+Maze.wall_char(False, self.v_walls[j][i]) for j in range(self.width-1)]) + '  |\n'
            s += '+' + ''.join([Maze.wall_char(True, self.h_walls[i][j])+'+' for j in range(self.width)]) + '\n'
        s += '|' + ''.join(['  '+Maze.wall_char(False, self.v_walls[j][-1]) for j in range(self.width-1)]) + '  |\n'
        s += '+' + (Maze.wall_char(True, True)+'+') * self.width
        return s

    @staticmethod
    def wall_char(horizontal, full):
        if full:
            return '--' if horizontal else '|'
        else:
            return '  ' if horizontal else ' '
