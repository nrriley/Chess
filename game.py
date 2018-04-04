def opposite_team(team_color):
    if team_color == "white":
        return "black"
    elif team_color == "black":
        return "white"
    else:
        return None


class Board:
    def __init__(self):
        self.grid = [[None for y in range(8)] for x in range(8)]
        pass

    def square_has_piece(self, x, y, team=None):
        if x > 7 or x < 0 or y > 7 or y < 0:
            return False

        if isinstance(self.grid[y][x], Piece):
            if team is None:
                return True
            elif team == self.grid[y][x].team:
                return True
            else:
                return False
        else:
            return False

    def display_board(self, highlight=[]):
        for y in range(8):
            for x in range(8):
                if isinstance(self.grid[y][x], Piece):
                    print(self.grid[y][x].icon, end=' ')
                else:
                    try:
                        highlight.index((x, y))
                        print('#', end=' ')
                    except ValueError:
                        print('+', end=' ')
            print('')


class Piece:
    def __init__(self):
        pass

    def valid_move_list():
        return []
