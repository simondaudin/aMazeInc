class Maze:

    def __init__(self, height, width, h_walls, v_walls):
        self.height = height
        self.width = width
        self.h_walls = h_walls
        self.v_walls = v_walls
        self.x_pos = 0
        self.y_pos = 0

    def __repr__(self):
        res = [list('+' + (Maze.wall_char(True, True) + '+') * self.width)]
        for i in range(self.height - 1):
            res.append(list('|' + ''.join(
                ['  ' + Maze.wall_char(False, self.v_walls[j][i]) for j in range(self.width - 1)]) + '  |'))
            res.append(list('+' + ''.join([Maze.wall_char(True, self.h_walls[i][j]) + '+' for j in range(self.width)])))
        res.append(list(
            '|' + ''.join(['  ' + Maze.wall_char(False, self.v_walls[j][-1]) for j in range(self.width - 1)]) + '  |'))
        res.append(list('+' + (Maze.wall_char(True, True) + '+') * self.width))
        if 0 <= self.x_pos < self.height and 0 <= self.y_pos < self.width:
            res[2 * self.x_pos + 1][3 * self.y_pos + 1] = 'X'
        return '\n'.join([''.join(line) for line in res])

    def set_pos(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def unset_pos(self):
        self.set_pos(-1, -1)

    @staticmethod
    def wall_char(horizontal, full):
        if full:
            return '--' if horizontal else '|'
        else:
            return '  ' if horizontal else ' '
