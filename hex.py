class HexTile:
    def __init__(self, a, r, c, type):
        self.a = a
        self.r = r
        self.c = c
        self.type = type

class HexBoard:
    def __init__(self):
        self.board = [[[]]] # board is a 3d array so hex types can be accessed easily,
                            # don't need to loop through the board to find a given hex tile
    
    def add_hex_tile(self, hex_tile):
        self.board[hex_tile.a][hex_tile.r][hex_tile.c] = type
    
    def get_hex_tile(self, a, r, c):
        try:
            return self.board[a][r][c]
        except IndexError:
            return None
    
    def get_neighbors(self, hex_tile):
        a = hex_tile.a
        r = hex_tile.r
        c = hex_tile.c
        top_left = self.get_hex_tile(1 - a, r - (1 - a), c - (1 - a))
        top_right = self.get_hex_tile(1 - a, r - (1 - a), c + a)
        left = self.get_hex_tile(a, r, c - 1)
        right = self.get_hex_tile(a, r, c + 1)
        bottom_left = self.get_hex_tile(1 - a, r + a, c - (1 - a))
        bottom_right = self.get_hex_tile(1 - a, r + a, c + a)

        return [top_left, top_right, left, right, bottom_left, bottom_right]

class PathSolver:
    pass