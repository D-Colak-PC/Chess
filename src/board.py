from consts import LIGHT_SQUARE_COLOR, DARK_SQUARE_COLOR, SELECTED_SQUARE_COLOR, SQUARE_SIZE, PIECES_TO_NAMES
import pieces

import pygame as pg
import numpy as np
from typing import Dict, Union, List


def draw_board(screen: pg.Surface) -> None:
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:  # Simplified condition for light squares
                color = LIGHT_SQUARE_COLOR
            else:
                color = DARK_SQUARE_COLOR
            
            pg.draw.rect(screen, pg.Color(color),
                         (col * SQUARE_SIZE,
                          row * SQUARE_SIZE,
                          SQUARE_SIZE,
                          SQUARE_SIZE))


def draw_selected_square(screen: pg.Surface, row: int, col: int) -> None:
    pg.draw.rect(screen, pg.Color(SELECTED_SQUARE_COLOR),
                 (col * SQUARE_SIZE,
                  row * SQUARE_SIZE,
                  SQUARE_SIZE,
                  SQUARE_SIZE))
    
    
def parse_FEN(fen: str) -> Dict[str, np.ndarray | str | List[bool] | str | int]:
    internal_board: np.ndarray = np.zeros((8, 8), dtype=object)
    fen_sections = fen.split(' ')
    
    for i, row in enumerate(fen_sections[0].split('/')):
        col = 0
        for char in row:
            if char.isdigit():
                col += int(char)
                continue
            
            if char.isupper():
                color = "white"
            else:
                color = "black"
            
            class_name = PIECES_TO_NAMES[char.lower()]
            piece = getattr(pieces, class_name)
            internal_board[i][col] = piece(color, i, col)
            # print(f"Placed {color} {class_name} at {i}, {col}")
            
            col += 1
    
    turn_to_move = fen_sections[1]
    if turn_to_move == 'w':
        turn_to_move = 'white'
    else:
        turn_to_move = 'black'
        
    castling_rights = fen_sections[2]
    white_castling_rights: List[bool] = ['K' in castling_rights, 'Q' in castling_rights]
    black_castling_rights: List[bool] = ['k' in castling_rights, 'q' in castling_rights]
    
    en_passant_target = fen_sections[3]
    halfmove_clock = int(fen_sections[4])
    fullmove_number = int(fen_sections[5])
    
    return {
        "internal board": internal_board,
        "turn to move": turn_to_move,
        "white castling rights": white_castling_rights,
        "black castling rights": black_castling_rights,
        "en passant target": en_passant_target,
        "halfmove clock": halfmove_clock,
        "fullmove number": fullmove_number
         }