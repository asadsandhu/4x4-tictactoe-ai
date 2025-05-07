import numpy as np
import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 4, 4
CELL_SIZE = WIDTH // BOARD_COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DEPTH_LIMIT = 3

class TicTacToe:
    def __init__(self, ai_first=False, use_alpha_beta=False):
        self.board = np.full((4, 4), '-')
        self.ai_first = ai_first
        self.use_alpha_beta = use_alpha_beta
        self.current_player = 'X' if not ai_first else 'O'
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic-Tac-Toe 4x4")
        self.window.fill(WHITE)
        self.draw_grid()
        self.nodes_expanded = 0

        if self.ai_first:
            self.ai_move()
    
    def draw_grid(self):
        for row in range(1, BOARD_ROWS):
            pygame.draw.line(self.window, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
        for col in range(1, BOARD_COLS):
            pygame.draw.line(self.window, BLACK, (col * CELL_SIZE, 0), (col * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.display.update()
    
    def draw_move(self, row, col):
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        if self.current_player == 'X':
            pygame.draw.line(self.window, RED, (center_x - 50, center_y - 50), (center_x + 50, center_y + 50), LINE_WIDTH)
            pygame.draw.line(self.window, RED, (center_x + 50, center_y - 50), (center_x - 50, center_y + 50), LINE_WIDTH)
        else:
            pygame.draw.circle(self.window, BLACK, (center_x, center_y), 50, LINE_WIDTH)
        pygame.display.update()
    
    def make_move(self, row, col):
        if self.board[row, col] == '-':
            self.board[row, col] = self.current_player
            self.draw_move(row, col)
            if self.is_winner(self.current_player):
                print(f"{self.current_player} wins!")
                pygame.quit()
                sys.exit()
            if self.is_full():
                print("The game is a draw!")
                pygame.quit()
                sys.exit()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            if self.current_player == 'O':
                self.ai_move()
    
    def is_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(4):
            if all(self.board[row][col] == player for row in range(4)):
                return True
        if all(self.board[i][i] == player for i in range(4)) or all(self.board[i][3 - i] == player for i in range(4)):
            return True
        return False
    
    def is_full(self):
        return '-' not in self.board
    
    def evaluate(self):
        if self.is_winner('O'):
            return 10
        if self.is_winner('X'):
            return -10
        return 0
    
    def minimax(self, depth, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        self.nodes_expanded += 1
        score = self.evaluate()
        if score == 10 or score == -10 or self.is_full() or depth >= DEPTH_LIMIT:
            return score
        
        if is_maximizing:
            best = float('-inf')
            for row in range(4):
                for col in range(4):
                    if self.board[row, col] == '-':
                        self.board[row, col] = 'O'
                        value = self.minimax(depth + 1, False, alpha, beta)
                        self.board[row, col] = '-'
                        best = max(best, value)
                        if self.use_alpha_beta:
                            alpha = max(alpha, best)
                            if beta <= alpha:
                                break
            return best
        else:
            best = float('inf')
            for row in range(4):
                for col in range(4):
                    if self.board[row, col] == '-':
                        self.board[row, col] = 'X'
                        value = self.minimax(depth + 1, True, alpha, beta)
                        self.board[row, col] = '-'
                        best = min(best, value)
                        if self.use_alpha_beta:
                            beta = min(beta, best)
                            if beta <= alpha:
                                break
            return best
    
    def ai_move(self):
        best_val = float('-inf')
        best_move = (-1, -1)
        self.nodes_expanded = 0
        start_time = time.time()
        
        for row in range(4):
            for col in range(4):
                if self.board[row, col] == '-':
                    self.board[row, col] = 'O'
                    move_val = self.minimax(0, False, float('-inf'), float('inf') if self.use_alpha_beta else None)
                    self.board[row, col] = '-'
                    if move_val > best_val:
                        best_move = (row, col)
                        best_val = move_val
        
        end_time = time.time()
        self.make_move(best_move[0], best_move[1])
        print(f"AI moved to {best_move}, Nodes Expanded: {self.nodes_expanded}, Time Taken: {end_time - start_time:.4f} sec")

if __name__ == "__main__":
    use_alpha_beta = input("Use Alpha-Beta Pruning? (y/n): ").strip().lower() == 'y'
    ai_first = input("Should AI go first? (y/n): ").strip().lower() == 'y'
    game = TicTacToe(ai_first=ai_first, use_alpha_beta=use_alpha_beta)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and game.current_player == 'X':
                x, y = event.pos
                row = y // CELL_SIZE
                col = x // CELL_SIZE
                game.make_move(row, col)
    pygame.quit()
