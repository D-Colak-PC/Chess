from .piece import Piece

import numpy as np
from typing import List, Tuple


class Bishop(Piece):
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)
        
        
    @staticmethod
    def get_valid_moves_from_pos(board: np.ndarray, color: str, row: int, col: int) -> List[Tuple[int, int]]:
        valid_moves: List[Tuple[int, int]] = []
        
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                new_x, new_y = row + dx, col + dy
                while 0 <= new_x < 8 and 0 <= new_y < 8:
                    if board[new_x][new_y] == 0:
                        valid_moves.append((new_x, new_y))
                    elif board[new_x][new_y].color != color:
                        valid_moves.append((new_x, new_y))
                        break
                    else:
                        break
                    new_x += dx
                    new_y += dy
        
        return valid_moves
    
    
    def get_valid_moves(self, board: np.ndarray) -> List[Tuple[int, int]]:
        valid_moves: List[Tuple[int, int]] = []
        
        for dx in [-1, 1]:
            for dy in [-1, 1]:
                new_x, new_y = self.row + dx, self.col + dy
                while 0 <= new_x < 8 and 0 <= new_y < 8:
                    if board[new_x][new_y] == 0:
                        valid_moves.append((new_x, new_y))
                    elif board[new_x][new_y].color != self.color:
                        valid_moves.append((new_x, new_y))
                        break
                    else:
                        break
                    new_x += dx
                    new_y += dy
        
        return valid_moves