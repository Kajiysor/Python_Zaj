import numpy as np
import random
import pygame
import sys
import math
from typing import List, Tuple


class Connect4():
    '''Connect 4 Game Class'''

    def __init__(self, ai_depth: int, row_count=6, column_count=7) -> None:
        ''' Initialize the gam '''

        # Variables for the game
        self.row_count = row_count
        self.column_count = column_count
        self.depth = ai_depth

        # Variables for the players
        self.player = 0
        self.ai = 1
        self.empty = 0
        self.__player_piece = 1
        self.__ai_piece = 2
        self.four_pieces = 4
        self.MAX = 100000000000000

        # Variables for the board
        self.board = np.zeros((self.row_count, self.column_count))
        self.__square_size = 100
        self.__radius = self.__square_size // 2 - 5
        self.__width = self.column_count * self.__square_size
        self.__height = (self.row_count + 1) * self.__square_size
        self.__turn = random.randint(self.player, self.ai)

        # Constants describing the colors
        self.__blue = (0, 0, 255)
        self.__black = (0, 0, 0)
        self.__red = (255, 0, 0)
        self.__yellow = (255, 255, 0)

    def __print_board(self, board: np.ndarray) -> None:
        ''' Prints the board to the console '''
        print(np.flip(board, 0))

    def __draw_board(self, board: np.ndarray, screen) -> None:
        ''' Draws the board to the screen '''
        for c in range(self.column_count):
            for r in range(self.row_count):
                pygame.draw.rect(
                    screen,
                    self.__blue,
                    (c *
                     self.__square_size,
                     r *
                     self.__square_size +
                     self.__square_size,
                     self.__square_size,
                     self.__square_size))
                pygame.draw.circle(
                    screen,
                    self.__black,
                    (c *
                     self.__square_size +
                     self.__square_size //
                     2,
                     r *
                     self.__square_size +
                     self.__square_size +
                     self.__square_size //
                     2),
                    self.__radius)

        for c in range(self.column_count):
            for r in range(self.row_count):
                if board[r][c] == self.__player_piece:
                    pygame.draw.circle(
                        screen, self.__red,
                        ((c *
                          self.__square_size +
                          self.__square_size //
                          2), self.__height -
                         (r *
                          self.__square_size +
                          self.__square_size //
                          2)), self.__radius)

                elif board[r][c] == self.__ai_piece:
                    pygame.draw.circle(
                        screen, self.__yellow,
                        ((c *
                          self.__square_size +
                          self.__square_size //
                          2), self.__height -
                         (r *
                          self.__square_size +
                          self.__square_size //
                          2)), self.__radius)

        pygame.display.update()

    def __drop_piece(self, board: np.ndarray, row: int,
                     col: int, piece: int) -> None:
        ''' Drops a piece in the specified row and column '''
        board[row][col] = piece

    def __is_valid_location(self, board: np.ndarray, col: int) -> bool:
        ''' Returns True if the specified column is valid '''
        return board[self.row_count - 1][col] == self.empty

    def __get_next_open_row(self, board: np.ndarray, col: int) -> int:
        '''
        Returns the row of the next available
        space in the specified colum
        '''
        for row in range(self.row_count):
            if board[row][col] == self.empty:
                return row

    def __get_valid_locations(self, board: np.ndarray) -> List[int]:
        ''' Returns a list of valid columns '''
        valid_locations = []

        for col in range(self.column_count):
            if self.__is_valid_location(board, col):
                valid_locations.append(col)

        return valid_locations

    def __eval_score_in_a_row(self, window: List[int], piece: int) -> int:
        ''' Returns the score of pieces in a row '''
        score = 0
        if piece == self.__player_piece:
            opponent_piece = self.__ai_piece
        else:
            opponent_piece = self.__player_piece

        if window.count(piece) == 4:
            score += 10000
        elif window.count(piece) == 3 and window.count(self.empty) == 1:
            score += 15
        elif window.count(piece) == 2 and window.count(self.empty) == 2:
            score += 5

        if (window.count(opponent_piece) == 3
                and window.count(self.empty) == 1):
            score -= 13

        return score

    def __eval_board_score(self, board: np.ndarray, piece: int) -> int:
        ''' Returns the score of the board '''
        score = 0

        # Score center column
        center_array = [i for i in list(board[:, self.column_count // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score horizontal
        for r in range(self.row_count):
            row_array = [i for i in list(board[r, :])]
            for c in range(self.column_count - 3):
                window = row_array[c:c + self.four_pieces]
                score += self.__eval_score_in_a_row(window, piece)

        # Score vertical
        for c in range(self.column_count):
            col_array = [i for i in list(board[:, c])]
            for r in range(self.row_count - 3):
                window = col_array[r:r + self.four_pieces]
                score += self.__eval_score_in_a_row(window, piece)

        # Score positive sloped diagonal
        for r in range(self.row_count - 3):
            for c in range(self.column_count - 3):
                window = ([board[r + i][c + i]
                          for i in range(self.four_pieces)])
                score += self.__eval_score_in_a_row(window, piece)

        # Score negative sloped diagonal
        for r in range(self.row_count - 3):
            for c in range(self.column_count - 3):
                window = [board[r + 3 - i][c + i]
                          for i in range(self.four_pieces)]
                score += self.__eval_score_in_a_row(window, piece)

        return score

    def __is_winning_move(self, board: np.ndarray, piece: int) -> bool:
        ''' Returns True if the move is a winning move '''

        # Check horizontal locations for win
        for c in range(self.column_count - 3):
            for r in range(self.row_count):
                if ((board[r][c] == piece)
                        and (board[r][c + 1] == piece)
                        and (board[r][c + 2] == piece)
                        and (board[r][c + 3] == piece)):
                    return True

        # Check vertical locations for win
        for c in range(self.column_count):
            for r in range(self.row_count - 3):
                if ((board[r][c] == piece)
                        and (board[r + 1][c] == piece)
                        and (board[r + 2][c] == piece)
                        and (board[r + 3][c] == piece)):
                    return True

        # Check positively sloped diaganols
        for c in range(self.column_count - 3):
            for r in range(self.row_count - 3):
                if ((board[r][c] == piece)
                        and (board[r + 1][c + 1] == piece)
                        and (board[r + 2][c + 2] == piece)
                        and (board[r + 3][c + 3] == piece)):
                    return True

        # Check negatively sloped diaganols
        for c in range(self.column_count - 3):
            for r in range(3, self.row_count):
                if ((board[r][c] == piece)
                        and (board[r - 1][c + 1] == piece)
                        and (board[r - 2][c + 2] == piece)
                        and (board[r - 3][c + 3] == piece)):
                    return True

    def __minimax(self, board: np.ndarray, depth: int, alpha=-math.inf,
                  beta=math.inf, maximizing_player=True) -> Tuple[int, int]:
        ''' Returns the best move for the AI '''

        valid_locations = self.__get_valid_locations(board)
        is_terminal = (
            self.__is_winning_move(
                board,
                self.__player_piece) or self.__is_winning_move(
                board,
                self.__ai_piece) or len(
                self.__get_valid_locations(board)) == 0)

        if depth == 0 or is_terminal:
            if is_terminal:
                if self.__is_winning_move(board, self.__ai_piece):
                    return (None, self.MAX)
                elif self.__is_winning_move(board, self.__player_piece):
                    return (None, -self.MAX)
                else:
                    return (None, 0)
            else:
                return (None, self.__eval_board_score(board, self.__ai_piece))

        if maximizing_player:
            value = -math.inf
            column = random.choice(valid_locations)

            for col in valid_locations:
                row = self.__get_next_open_row(board, col)
                b_copy = board.copy()
                self.__drop_piece(b_copy, row, col, self.__ai_piece)
                new_score = self.__minimax(
                    b_copy, depth - 1, alpha, beta, False)[1]

                if new_score > value:
                    value = new_score
                    column = col

                alpha = max(alpha, value)

                if alpha >= beta:
                    break

            return column, value

        else:
            value = math.inf
            column = random.choice(valid_locations)

            for col in valid_locations:
                row = self.__get_next_open_row(board, col)
                b_copy = board.copy()
                self.__drop_piece(b_copy, row, col, self.__player_piece)
                new_score = self.__minimax(
                    b_copy, depth - 1, alpha, beta, True)[1]

                if new_score < value:
                    value = new_score
                    column = col

                beta = min(beta, value)

                if alpha >= beta:
                    break

            return column, value

    def play_game(self) -> None:
        self.__print_board(self.board)
        game_over = False

        pygame.init()
        screen = pygame.display.set_mode((self.__width, self.__height))
        self.__draw_board(self.board, screen)
        pygame.display.update()
        myfont = pygame.font.SysFont("monospace", 75)

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, self.__black,
                                     (0, 0, self.__width, self.__square_size))
                    posx = event.pos[0]
                    if self.__turn == 0:
                        pygame.draw.circle(screen, self.__red, (posx, (
                            self.__square_size // 2)), self.__radius)

                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, self.__black,
                                     (0, 0, self.__width, self.__square_size))

                    # Ask for Player 1 Input
                    if self.__turn == 0:
                        posx = event.pos[0]
                        col = math.floor(posx / self.__square_size)

                        if self.__is_valid_location(self.board, col):
                            row = self.__get_next_open_row(self.board, col)
                            self.__drop_piece(self.board, row,
                                              col, self.__player_piece)

                            if self.__is_winning_move(
                                    self.board, self.__player_piece):
                                label = myfont.render(
                                    "Player 1 wins!", 1, self.__red)
                                screen.blit(label, (40, 10))
                                game_over = True

                            self.__turn = (self.__turn + 1) % 2

                            self.__print_board(self.board)
                            self.__draw_board(self.board, screen)

            # Ask for Player 2 Input
            if self.__turn == 1 and not game_over:

                col = self.__minimax(self.board, self.depth)[0]

                if self.__is_valid_location(self.board, col):
                    row = self.__get_next_open_row(self.board, col)
                    self.__drop_piece(self.board, row, col, self.__ai_piece)

                    if self.__is_winning_move(self.board, self.__ai_piece):
                        label = myfont.render(
                            "Player 2 wins!", 1, self.__yellow)
                        screen.blit(label, (40, 10))
                        game_over = True

                    self.__turn = (self.__turn + 1) % 2

                    self.__print_board(self.board)
                    self.__draw_board(self.board, screen)

            if game_over:
                pygame.time.wait(3000)


if __name__ == "__main__":
    Connect4(ai_depth=5).play_game()
