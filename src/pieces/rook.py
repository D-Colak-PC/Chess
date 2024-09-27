from .piece import Piece

import numpy as np
from typing import List, Tuple


class Rook(Piece):
    def __init__(self, color: str, x: int, y: int):
        super().__init__(color, x, y)
    

    @staticmethod
    def get_valid_moves_from_pos(board: np.ndarray, color: str, row: int, col: int) -> List[Tuple[int, int]]:
        valid_moves: List[Tuple[int, int]] = []
        
        # horizontal moves
        for dx in [-1, 1]: # left and right
            new_x, new_y = row, col + dx
            while 0 <= new_y < 8: # check if the new position is within the board
                if board[new_x][new_y] == 0: # if the square is empty
                    valid_moves.append((new_x, new_y)) # add the square to the list of valid moves
                elif board[new_x][new_y].color != color: # if the square is occupied by an enemy piece
                    valid_moves.append((new_x, new_y)) # add the square to the list of valid moves
                    break # we can't move any further
                else:
                    break
                new_y += dx
        
        # vertical moves
        for dy in [-1, 1]:
            new_x, new_y = row + dy, col
            while 0 <= new_x < 8:
                if board[new_x][new_y] == 0:
                    valid_moves.append((new_x, new_y))
                elif board[new_x][new_y].color != color:
                    valid_moves.append((new_x, new_y))
                    break
                else:
                    break
                new_x += dy
        
        return valid_moves
    

    def get_valid_moves(self, board: np.ndarray) -> List[Tuple[int, int]]:
        valid_moves: List[Tuple[int, int]] = []
        
        # horizontal moves
        for dx in [-1, 1]: # left and right
            new_x, new_y = self.row, self.col + dx
            while 0 <= new_y < 8: # check if the new position is within the board
                if board[new_x][new_y] == 0: # if the square is empty
                    valid_moves.append((new_x, new_y)) # add the square to the list of valid moves
                elif board[new_x][new_y].color != self.color: # if the square is occupied by an enemy piece
                    valid_moves.append((new_x, new_y)) # add the square to the list of valid moves
                    break # we can't move any further
                else:
                    break
                new_y += dx
        
        # vertical moves
        for dy in [-1, 1]:
            new_x, new_y = self.row + dy, self.col
            while 0 <= new_x < 8:
                if board[new_x][new_y] == 0:
                    valid_moves.append((new_x, new_y))
                elif board[new_x][new_y].color != self.color:
                    valid_moves.append((new_x, new_y))
                    break
                else:
                    break
                new_x += dy
        
        return valid_moves