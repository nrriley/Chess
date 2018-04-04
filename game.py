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
        # Defining custom exception.
        class InvalidMoveError(Exception):
            pass

        if isinstance(p, Piece) is False:
            raise TypeError("move_piece() tried to move not a piece")

        # Test if requested move destination is valid per the rules of chess.
        try:
            p.valid_move_list(self).index((dest_x, dest_y))
        except ValueError:
            raise InvalidMoveError(
                    "move_piece() tried to move piece to invalid destination" +
                    "\nvalid moves: " + str(p.valid_move_list(self)) +
                    "\ntried: (" + str(dest_x) + ", " + str(dest_y) + ")")
        else:
            # Setting return values
            captured_piece = self.grid[dest_y][dest_x]
            old_x, old_y = p.x, p.y
            # Updating board
            self.grid[dest_y][dest_x] = p
            self.grid[p.y][p.x] = None

        # Check if piece captured was passant and remove pawn if true
        if isinstance(captured_piece, Passant):
            captured_piece = self.grid[p.y][dest_x]
            self.grid[p.y][dest_x] = None

        # Remove old passants
        for i in range(8):
            if isinstance(self.grid[2][i], Passant):
                self.grid[2][i] = None
            if isinstance(self.grid[5][i], Passant):
                self.grid[5][i] = None

        # If a pawn was double moved, create special 'passant' piece in the
        # square it moved over
        if (dest_x == p.x) and (
           (dest_y is 3 and p.y is 1 and p.has_moved is False) or
           (dest_y is 4 and p.y is 6 and p.has_moved is False)):
            print("Passant created at: (" +
                  str(p.x) + ", " +
                  str((dest_y+p.y)//2)+")")
            pas = Passant(p.x, (dest_y+p.y)//2, p.team)
            self.grid[(dest_y+p.y)//2][p.x] = pas

        # Updating fields of piece that moved
        p.x, p.y = dest_x, dest_y
        p.has_moved = True

        return captured_piece, old_x, old_y, dest_x, dest_y


class Piece:
    def __init__(self):
        pass

    def valid_move_list(self, board):
        return []


class Passant(Piece):
    def __init__(self, x, y, team):
        self.team = team
        self.icon = 'X'
        self.x = x
        self.y = y
