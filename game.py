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

        # Setup Pawns
        for i in range(8):
            self.grid[6][i] = PawnW(i, 6)
            self.grid[1][i] = PawnB(i, 1)

        # Setup Rooks
        self.grid[0][0] = Rook(0, 0, "black")
        self.grid[0][7] = Rook(7, 0, "black")
        self.grid[7][0] = Rook(0, 7, "white")
        self.grid[7][7] = Rook(7, 7, "white")

        # Setup Knights

        # Setup Bishops
        self.grid[0][2] = Bishop(2, 0, "black")
        self.grid[0][5] = Bishop(5, 0, "black")
        self.grid[7][2] = Bishop(2, 7, "white")
        self.grid[7][5] = Bishop(5, 7, "white")

        # Setup Queens
        self.grid[0][3] = Queen(3, 0, "black")
        self.grid[7][3] = Queen(3, 7, "white")

        # Setup Kings

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


class PawnW(Piece):
    def __init__(self, x, y):
        self.team = "white"
        self.icon = '♟'
        self.x = x
        self.y = y

    def valid_move_list(self, b):
        valid_moves = []

        if isinstance(b, Board) is False:
            return valid_moves

        # Check if another piece is blocking path
        if b.square_has_piece(self.x, self.y-1) is False:
            valid_moves.append((self.x, self.y-1))

        # Check if another piece can be taken diagonally
        if b.square_has_piece(self.x+1, self.y-1, opposite_team(self.team)):
            valid_moves.append((self.x+1, self.y-1))
        if b.square_has_piece(self.x-1, self.y-1, opposite_team(self.team)):
            valid_moves.append((self.x-1, self.y-1))

        # TODO: en passant
        # TODO: double moves

        for i in valid_moves:
            if i[0] < 0 or i[1] < 0:
                del valid_moves[i]

        return valid_moves


class PawnB(Piece):
    def __init__(self, x, y):
        self.team = "black"
        self.icon = '♟'
        self.x = x
        self.y = y

    def valid_move_list(self, b):
        valid_moves = []

        if isinstance(b, Board) is False:
            return valid_moves

        # Check if another piece is blocking path
        if b.square_has_piece(self.x, self.y+1) is False:
            valid_moves.append((self.x, self.y+1))

        # Check if piece can be taken diagonally
        if b.square_has_piece(self.x+1, self.y+1, opposite_team(self.team)):
            valid_moves.append((self.x+1, self.y+1))
        if b.square_has_piece(self.x-1, self.y+1, opposite_team(self.team)):
            valid_moves.append((self.x-1, self.y+1))

        # TODO: en passant
        # TODO: double moves

        for i in valid_moves:
            if i[0] < 0 or i[1] < 0:
                del valid_moves[i]

        return valid_moves


class Rook(Piece):
    def __init__(self, x, y, team):
        self.team = team
        self.icon = '♜'
        self.x = x
        self.y = y

    def valid_move_list(self, b):
        valid_moves = []

        if isinstance(b, Board) is False:
            return valid_moves

        # Check for valid moves in up direction.
        for y in range(self.y-1, -1, -1):
            if b.square_has_piece(self.x, y) is False:
                valid_moves.append((self.x, y))
            elif b.square_has_piece(self.x, y, opposite_team(self.team)):
                valid_moves.append((self.x, y))
                break
            else:
                break

        # Check for valid moves in down direction.
        for y in range(self.y+1, 8):
            if b.square_has_piece(self.x, y) is False:
                valid_moves.append((self.x, y))
            elif b.square_has_piece(self.x, y, opposite_team(self.team)):
                valid_moves.append((self.x, y))
                break
            else:
                break

        # Check for valid moves in left direction.
        for x in range(self.x-1, -1, -1):
            if b.square_has_piece(x, self.y) is False:
                valid_moves.append((x, self.y))
            elif b.square_has_piece(x, self.y, opposite_team(self.team)):
                valid_moves.append((x, self.y))
                break
            else:
                break

        # Check for valid moves in right direction.
        for x in range(self.x+1, 8):
            if b.square_has_piece(x, self.y) is False:
                valid_moves.append((x, self.y))
            elif b.square_has_piece(x, self.y, opposite_team(self.team)):
                valid_moves.append((x, self.y))
                break
            else:
                break

        for i in valid_moves:
            if i[0] < 0 or i[1] < 0:
                del valid_moves[i]

        return valid_moves


class Bishop(Piece):
    def __init__(self, x, y, team):
        self.team = team
        self.icon = '♝'
        self.x = x
        self.y = y

    def valid_move_list(self, b):
        valid_moves = []

        if isinstance(b, Board) is False:
            return valid_moves

        # Check for valid moves in up-left direction.
        for x, y in zip(range(self.x-1, -1, -1), range(self.y-1, -1, -1)):
            if b.square_has_piece(x, y) is False:
                valid_moves.append((x, y))
            elif b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))
                break
            else:
                break

        # Check for valid moves in up-right direction.
        for x, y in zip(range(self.x+1, 8), range(self.y-1, -1, -1)):
            if b.square_has_piece(x, y) is False:
                valid_moves.append((x, y))
            elif b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))
                break
            else:
                break

        # Check for valid moves in down-left direction.
        for x, y in zip(range(self.x-1, -1, -1), range(self.y+1, 8)):
            if b.square_has_piece(x, y) is False:
                valid_moves.append((x, y))
            elif b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))
                break
            else:
                break

        # Check for valid moves in down-right direction.
        for x, y in zip(range(self.x+1, 8), range(self.y+1, 8)):
            if b.square_has_piece(x, y) is False:
                valid_moves.append((x, y))
            elif b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))
                break
            else:
                break

        for i in valid_moves:
            if i[0] < 0 or i[1] < 0:
                del valid_moves[i]

        return valid_moves


class Queen(Piece):
    def __init__(self, x, y, team):
        self.team = team
        self.icon = '♛'
        self.x = x
        self.y = y

    def valid_move_list(self, b):
        valid_moves = []

        if isinstance(b, Board) is False:
            return valid_moves

        # Check for valid moves in up direction.
        for y in range(self.y-1, -1, -1):
            if b.square_has_piece(self.x, y) is False:
                valid_moves.append((self.x, y))
            elif b.square_has_piece(self.x, y, opposite_team(self.team)):
                valid_moves.append((self.x, y))
                break
            else:
                break

        # Check for valid moves in down direction.
        for y in range(self.y+1, 8):
            if b.square_has_piece(self.x, y) is False:
                valid_moves.append((self.x, y))
            elif b.square_has_piece(self.x, y, opposite_team(self.team)):
                valid_moves.append((self.x, y))
                break
            else:
                break

        # Check for valid moves in left direction.
        for x in range(self.x-1, -1, -1):
            if b.square_has_piece(x, self.y) is False:
                valid_moves.append((x, self.y))
            elif b.square_has_piece(x, self.y, opposite_team(self.team)):
                valid_moves.append((x, self.y))
                break
            else:
                break

        # Check for valid moves in right direction.
        for x in range(self.x+1, 8):
            if b.square_has_piece(x, self.y) is False:
                valid_moves.append((x, self.y))
            elif b.square_has_piece(x, self.y, opposite_team(self.team)):
                valid_moves.append((x, self.y))
                break
            else:
                break

        # Check for valid moves in up-left direction.
        for x, y in zip(range(self.x-1, -1, -1), range(self.y-1, -1, -1)):
            if b.square_has_piece(x, y) is False:
                valid_moves.append((x, y))
            elif b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))
                break
            else:
                break

        # Check for valid moves in up-right direction.
        for x, y in zip(range(self.x+1, 8), range(self.y-1, -1, -1)):
            if b.square_has_piece(x, y) is False:
                valid_moves.append((x, y))
            elif b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))
                break
            else:
                break

        # Check for valid moves in down-left direction.
        for x, y in zip(range(self.x-1, -1, -1), range(self.y+1, 8)):
            if b.square_has_piece(x, y) is False:
                valid_moves.append((x, y))
            elif b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))
                break
            else:
                break

        # Check for valid moves in down-right direction.
        for x, y in zip(range(self.x+1, 8), range(self.y+1, 8)):
            if b.square_has_piece(x, y) is False:
                valid_moves.append((x, y))
            elif b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))
                break
            else:
                break

        for i in valid_moves:
            if i[0] < 0 or i[1] < 0:
                del valid_moves[i]

        return valid_moves
