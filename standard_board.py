from game import Board
import standard_pieces as sp


class StandardBoard(Board):
    def __init__(self):
        self.grid = [[None for y in range(8)] for x in range(8)]

        # Setup Pawns
        for i in range(8):
            self.grid[6][i] = sp.PawnW(i, 6)
            self.grid[1][i] = sp.PawnB(i, 1)

        # Setup Rooks
        self.grid[0][0] = sp.Rook(0, 0, "black")
        self.grid[0][7] = sp.Rook(7, 0, "black")
        self.grid[7][0] = sp.Rook(0, 7, "white")
        self.grid[7][7] = sp.Rook(7, 7, "white")

        # Setup Knights
        self.grid[0][1] = sp.Knight(1, 0, "black")
        self.grid[0][6] = sp.Knight(6, 0, "black")
        self.grid[7][1] = sp.Knight(1, 7, "white")
        self.grid[7][6] = sp.Knight(6, 7, "white")

        # Setup Bishops
        self.grid[0][2] = sp.Bishop(2, 0, "black")
        self.grid[0][5] = sp.Bishop(5, 0, "black")
        self.grid[7][2] = sp.Bishop(2, 7, "white")
        self.grid[7][5] = sp.Bishop(5, 7, "white")

        # Setup Queens
        self.grid[0][3] = sp.Queen(3, 0, "black")
        self.grid[7][3] = sp.Queen(3, 7, "white")

        # Setup Kings
        self.grid[0][4] = sp.King(3, 0, "black")
        self.grid[7][4] = sp.King(3, 7, "white")
