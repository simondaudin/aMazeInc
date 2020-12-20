class Maze:

    def __init__(self, height, width, h_walls, v_walls):
        self.height = height
        self.width = width
        self.h_walls = h_walls
        self.v_walls = v_walls

    def representation(self):
        res = [list('+' + (Maze.wall_char(True, True) + '+') * self.width)]
        for i in range(self.height - 1):
            res.append(list('|' + ''.join(
                ['  ' + Maze.wall_char(False, self.v_walls[j][i]) for j in range(self.width - 1)]) + '  |'))
            res.append(list('+' + ''.join([Maze.wall_char(True, self.h_walls[i][j]) + '+' for j in range(self.width)])))
        res.append(list(
            '|' + ''.join(['  ' + Maze.wall_char(False, self.v_walls[j][-1]) for j in range(self.width - 1)]) + '  |'))
        res.append(list('+' + (Maze.wall_char(True, True) + '+') * self.width))
        return res

    def print_with_post(self, pos_x, pos_y):
        r = self.representation()
        if 0 < pos_x < self.height and 0 < pos_y < self.width:
            r[2 * pos_x + 1][3 * pos_y + 1] = 'X'
        return '\n'.join([''.join(line) for line in r])

    def __repr__(self):
        return self.print_with_post(-1, -1)

    @staticmethod
    def wall_char(horizontal, full):
        if full:
            return '--' if horizontal else '|'
        else:
            return '  ' if horizontal else ' '
