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

    def move_piece(self, p, dest_x, dest_y):
        class InvalidMoveError(Exception):
            pass

        if isinstance(p, Piece) is False:
            raise TypeError("move_piece() tried to move not a piece")

        try:
            p.valid_move_list(self).index((dest_x, dest_y))
        except ValueError:
            raise InvalidMoveError(
                    "move_piece() tried to move piece to invalid destination\n" +
                    "valid moves: " + str(p.valid_move_list(self)) +
                    "\ntried: (" + str(dest_x) + ", " + str(dest_y) + ")")
        else:
            # Setting return values
            captured_piece = self.grid[dest_y][dest_x]
            old_x, old_y = p.x, p.y
            # Updating board
            self.grid[dest_y][dest_x] = p
            self.grid[p.y][p.x] = None
            # Updating piece
            p.x, p.y = dest_x, dest_y

        p.has_moved = True

        return captured_piece, old_x, old_y, dest_x, dest_y


class Piece:
    def __init__(self):
        pass

    def valid_move_list():
        return []
