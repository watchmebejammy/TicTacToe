import random

class TicTacToe:
    def __init__(self):
        self.board = []
    
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
    
    def random_first_player(self):
        return random.randomint(0, 1)
    
    def fix_spot(self, row, col, player):
        self.board[row][col] = player
    
    def is_player_win(self,player):
        win = None
        
        n = len(self.board)
        
        
        # Checking rows 
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
            
        # Checking Columns
        for i in range(n):
            win = True 
            for j in range(n)
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
            
        #Checking Diagonals
        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
            return True
    
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
                return True
        