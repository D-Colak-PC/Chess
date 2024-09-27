from consts import SQUARE_SIZE, NAMES_TO_PIECES, VALID_SQUARE_COLOR, VALID_SQUARE_DOT_RADIUS

import numpy as np
import pygame as pg
import pygame.gfxdraw as gfxdraw
from pathlib import Path

class Piece:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.last_row = row
        self.last_col = col
        self.x = self.col * SQUARE_SIZE
        self.y = self.row * SQUARE_SIZE
        self.dir = -1 if self.color == "white" else 1
        self.moved = False
        self.selected = False
        self.image_file_name = self.color[0] + NAMES_TO_PIECES[self.__class__.__name__].upper()
        self.image = self._scale_png()
        
    def _generate_image_file_path(self):
        file_path = Path(__file__).resolve().parents[2] / "assets" / "img" / "png" / self.color / f"{self.image_file_name}.png"
        # print(f"Image file path: {file_path}")
        return file_path
    
    def _scale_png(self):
        image = pg.image.load(self._generate_image_file_path())
        image = pg.transform.smoothscale(image, (SQUARE_SIZE, SQUARE_SIZE))
        
        return image
    
    def get_valid_moves(self, board):
        raise NotImplementedError
    
    def is_valid_move(self, board, row, col):
        valid_moves = self.get_valid_moves(board)
        return (row, col) in valid_moves
    
    def draw_valid_moves(self, screen, valid_moves):
        for move in valid_moves:
            row, col = move
            gfxdraw.filled_circle(
                screen,
                col * SQUARE_SIZE + SQUARE_SIZE // 2,
                row * SQUARE_SIZE + SQUARE_SIZE // 2,
                VALID_SQUARE_DOT_RADIUS,
                pg.Color(VALID_SQUARE_COLOR)
                )
            gfxdraw.aacircle(
                screen,
                col * SQUARE_SIZE + SQUARE_SIZE // 2,
                row * SQUARE_SIZE + SQUARE_SIZE // 2,
                VALID_SQUARE_DOT_RADIUS,
                pg.Color(VALID_SQUARE_COLOR)
                )
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
    def follow_mouse(self, screen, mouse_pos):
        self.x, self.y = mouse_pos
        screen.blit(self.image, (self.x - SQUARE_SIZE // 2, self.y - SQUARE_SIZE // 2))
    
    def move(self, row, col):
        self.last_row = self.row
        self.last_col = self.col
        self.row = row
        self.col = col
        self.x = self.col * SQUARE_SIZE
        self.y = self.row * SQUARE_SIZE
        
        self.moved = True
    
    def select(self):
        self.selected = True
    
    def deselect(self):
        self.selected = False
        
        col = self.x // SQUARE_SIZE
        row = self.y // SQUARE_SIZE
        
        self.move(row, col)

    def remove_selection(self):
        self.selected = False
        
        self.x = self.col * SQUARE_SIZE
        self.y = self.row * SQUARE_SIZE
    
    def __repr__(self):
        name = NAMES_TO_PIECES[self.__class__.__name__]
        return f"{(name.upper() if self.color == 'white' else name.lower())[0]}"
    
    def __str__(self):
        return f"{self.color} {self.__class__.__name__} at ({self.row}, {self.col})"