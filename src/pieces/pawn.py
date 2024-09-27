from .piece import Piece

class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        
    def get_valid_moves(self, board):
        valid_moves = []
        
        new_x, new_y = self.row + self.dir, self.col # move one square forward
        if 0 <= new_x < 8: # check if the new position is within the board
            if board[new_x][new_y] == 0: # cant capture a piece
                valid_moves.append((new_x, new_y))
            
            if self.row == 1 and self.color == "black" or self.row == 6 and self.color == "white": # check if the pawn is in the starting position
                new_x = self.row + 2 * self.dir # move two squares forward
                if board[new_x][new_y] == 0 and board[self.row + self.dir][new_y] == 0: # cant capture a piece
                    valid_moves.append((new_x, new_y))
        
        # diagonal catpures
        for dx in [-1, 1]:
            new_x, new_y = self.row + self.dir, self.col + dx # move one square forward and one square to the left or right
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board[new_x][new_y] != 0 and board[new_x][new_y].color != self.color: # now we can capture
                    valid_moves.append((new_x, new_y))
        
        return valid_moves