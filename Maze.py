class Maze:

    def __init__(self, height, width, h_walls, v_walls):
        self.height = height
        self.width = width
        self.h_walls = h_walls
        self.v_walls = v_walls

    def __repr__(self):
        s = ' ' + '_' * (2 * self.width - 1) + ' ' + '\n'
        for i in range(self.height - 1):
            s += '|'
            for j in range(self.width - 1):
                s += Maze.wall_char(True, self.h_walls[i][j])
                s += Maze.wall_char(False, self.v_walls[j][i])
            s += Maze.wall_char(True, self.h_walls[i][-1])
            s += '|\n'
        s += '|'
        for j in range(self.width - 1):
            s += '_'
            s += Maze.wall_char(False, self.v_walls[j][-1])
        s += '_|'
        return s

    @staticmethod
    def wall_char(horizontal, full):
        if full:
            return '_' if horizontal else '|'
        else:
            return ' '
