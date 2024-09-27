import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

from consts import *
from board import draw_board, parse_FEN, draw_selected_square
from sound import play_effect

import pygame as pg



def main():
    
    parsed_FEN = parse_FEN(STARTING_POSITION)
    internal_board = parsed_FEN["internal board"]
    turn_to_move = parsed_FEN["turn to move"]
    halfmove_clock = parsed_FEN["halfmove clock"]
    fullmove_number = parsed_FEN["fullmove number"]

    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pg.display.set_caption(WINDOW_TITLE)
    # print("Pygame window started")
    play_effect("game_start")
    
    coordinates_of_last_piece = [-1, -1]
    piece_selected = False
    
    running = True
    while running:
        
        mouse_pos = pg.mouse.get_pos()
        mouse_col = mouse_pos[0] // SQUARE_SIZE
        mouse_row = mouse_pos[1] // SQUARE_SIZE
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
            # selecting a piece
            if event.type == pg.MOUSEBUTTONDOWN:
                if internal_board[mouse_row][mouse_col] == 0:
                    # print("Invalid selection: no piece there")
                    continue
                
                if internal_board[mouse_row][mouse_col].color != turn_to_move:
                    # print(f"Invalid selection: {turn_to_move} to move")
                    continue
                
                coordinates_of_last_piece = [mouse_row, mouse_col]
                internal_board[mouse_row][mouse_col].select()
                piece_selected = True
                # print(f"Selected piece: {internal_board[coordinates_of_last_piece[0]][coordinates_of_last_piece[1]]}")
                # print(f"Valid moves: {internal_board[coordinates_of_last_piece[0]][coordinates_of_last_piece[1]].get_valid_moves(internal_board)}")
                
            # releasing a piece
            if event.type == pg.MOUSEBUTTONUP:
                if not piece_selected:
                    continue
                
                if not internal_board[coordinates_of_last_piece[0]][coordinates_of_last_piece[1]].is_valid_move(internal_board, mouse_row, mouse_col):
                    # print("Invalid move: piece can't move there")
                    # print(f"Mouse Coords: {mouse_row}, {mouse_col}")
                    internal_board[coordinates_of_last_piece[0]][coordinates_of_last_piece[1]].remove_selection()
                    play_effect("illegal")
                    
                else:
                    # print("Valid move")
                    if internal_board[mouse_row][mouse_col] != 0:
                        play_effect("capture")
                    elif turn_to_move == "white":
                        play_effect("move_self")
                    elif turn_to_move == "black":
                        play_effect("move_opponent")
                    
                    internal_board[mouse_row][mouse_col] = internal_board[coordinates_of_last_piece[0]][coordinates_of_last_piece[1]]
                    internal_board[mouse_row][mouse_col].deselect()
                    internal_board[coordinates_of_last_piece[0]][coordinates_of_last_piece[1]] = 0
                    coordinates_of_last_piece = [mouse_row, mouse_col]
                    # print(f"board state:\n{internal_board}")
                    
                    halfmove_clock += 1
                    halfmove_clock %= 2
                    
                    if turn_to_move == "white":
                        turn_to_move = "black"
                    else:
                        turn_to_move = "white"
                        fullmove_number += 1
                        
                    # print(f"halfmove clock: {halfmove_clock}, fullmove number: {fullmove_number}")
            
                piece_selected = False
                                        
        # draw the board
        draw_board(screen)
        
        # draw selected squares
        if coordinates_of_last_piece != [-1, -1]:
            draw_selected_square(screen, coordinates_of_last_piece[0], coordinates_of_last_piece[1])
            last_piece = internal_board[coordinates_of_last_piece[0]][coordinates_of_last_piece[1]]
            draw_selected_square(screen, last_piece.last_row, last_piece.last_col)
        
        # draw non-selected pieces
        for row in internal_board:
            for piece in row:
                if piece != 0 and not piece.selected:
                    piece.draw(screen)
        
        # draw valid moves and follow mouse for the selected piece
        for row in internal_board:
            for piece in row:
                if piece != 0 and piece.selected:
                    piece.draw_valid_moves(screen, piece.get_valid_moves(internal_board))
                    piece.follow_mouse(screen, mouse_pos)
                        
        pg.display.flip()
        
        
if __name__ == '__main__':
    # print("Program started")
    main()
    