from game import Board, Piece, opposite_team


class PawnW(Piece):
    def __init__(self, x, y):
        self.team = "white"
        self.icon = '♟'
        self.x = x
        self.y = y
        self.has_moved = False

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

        # Double Moves
        if self.has_moved is False and \
           b.square_has_piece(self.x, self.y-1) is False and \
           b.square_has_piece(self.x, self.y-2) is False:
            valid_moves.append((self.x, self.y-2))

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
        self.has_moved = False

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

        # Double Moves
        if self.has_moved is False and \
           b.square_has_piece(self.x, self.y+1) is False and \
           b.square_has_piece(self.x, self.y+2) is False:
            valid_moves.append((self.x, self.y+2))

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


class Knight(Piece):
    def __init__(self, x, y, team):
        self.team = team
        self.icon = '♞'
        self.x = x
        self.y = y

    def valid_move_list(self, b):
        valid_moves = []

        if isinstance(b, Board) is False:
            return valid_moves

        for x, y in [(self.x+1, self.y-2),   # Up-Up-R
                     (self.x+2, self.y-1),   # Up-R-R
                     (self.x+2, self.y+1),   # Down-R-R
                     (self.x+1, self.y+2),   # Down-Down-R
                     (self.x-1, self.y+2),   # Down-Down-L
                     (self.x-2, self.y+1),   # Down-L-L
                     (self.x-2, self.y-1),   # Up-L-L
                     (self.x-1, self.y-2)]:  # Up-Up-L
            if b.square_has_piece(x, y) is False or \
               b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))

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


class King(Piece):
    def __init__(self, x, y, team):
        self.team = team
        self.icon = '♚'
        self.x = x
        self.y = y

    def valid_move_list(self, b):
        valid_moves = []

        if isinstance(b, Board) is False:
            return valid_moves

        for x, y in [(self.x  , self.y-1),   # Up
                     (self.x+1, self.y-1),   # Up-R
                     (self.x+1, self.y  ),   # R
                     (self.x+1, self.y+1),   # Down-R
                     (self.x  , self.y+1),   # Down
                     (self.x-1, self.y+1),   # Down-L
                     (self.x-1, self.y  ),   # L
                     (self.x-1, self.y-1)]:  # Up-L
            if b.square_has_piece(x, y) is False or \
               b.square_has_piece(x, y, opposite_team(self.team)):
                valid_moves.append((x, y))

        # TODO: Castling
        return valid_moves
