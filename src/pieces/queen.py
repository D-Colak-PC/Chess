from .piece import Piece
from .rook import Rook
from .bishop import Bishop


class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        
    def get_valid_moves(self, board):
        valid_moves = Rook.get_valid_moves_from_pos(board, self.color, self.row, self.col) + Bishop.get_valid_moves_from_pos(board, self.color, self.row, self.col)
        
        return valid_moves