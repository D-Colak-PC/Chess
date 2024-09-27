from .piece import Piece

import numpy as np
from typing import List, Tuple


class King(Piece):
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)
      
        
    def get_valid_moves(self, board: np.ndarray) -> List[Tuple[int, int]]:
        deltas: List[Tuple[int, int]] = [(-1, -1), (-1, 0 ), (-1, 1 ),
                                         (0 , -1),           (0 , 1 ),
                                         (1 , -1), (1 , 0 ), (1 , 1 )]
        
        valid_moves: List[Tuple[int, int]] = []
        
        for dx, dy in deltas:
            new_x, new_y = self.row + dx, self.col + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board[new_x][new_y] == 0 or board[new_x][new_y].color != self.color:
                    valid_moves.append((new_x, new_y))
        
        return valid_moves
                