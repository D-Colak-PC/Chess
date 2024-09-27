from .piece import Piece

class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        
    def get_valid_moves(self, board):
        deltas = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
        
        valid_moves = []
        
        for dx, dy in deltas:
            new_x, new_y = self.row + dx, self.col + dy
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board[new_x][new_y] == 0 or board[new_x][new_y].color != self.color:
                    valid_moves.append((new_x, new_y))
        
        return valid_moves