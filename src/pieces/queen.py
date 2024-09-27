from .piece import Piece
from .rook import Rook
from .bishop import Bishop

import numpy as np
from typing import List, Tuple


class Queen(Piece):
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)
        
        
    def get_valid_moves(self, board: np.ndarray) -> List[Tuple[int, int]]:
        valid_moves = Rook.get_valid_moves_from_pos(board, self.color, self.row, self.col) + Bishop.get_valid_moves_from_pos(board, self.color, self.row, self.col)
        
        return valid_moves