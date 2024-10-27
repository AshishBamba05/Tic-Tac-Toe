def check_winner(self):
        # Check rows, columns, and depths
        for i in range(3):
            for j in range(3):
                if (self.board[i, j, :].sum() == 3 or 
                    self.board[i, :, j].sum() == 3 or 
                    self.board[:, i, j].sum() == 3):
                    return 1  # Player 1 wins
                if (self.board[i, j, :].sum() == -3 or 
                    self.board[i, :, j].sum() == -3 or 
                    self.board[:, i, j].sum() == -3):
                    return -1  # Player 2 wins

 # Check diagonals
        for i in range(3):
            if (self.board[i, i, :].sum() == 3 or 
                self.board[i, :, i].sum() == 3 or 
                self.board[:, i, i].sum() == 3):
                return 1  # Player 1 wins
            if (self.board[i, i, :].sum() == -3 or 
                self.board[i, :, i].sum() == -3 or 
                self.board[:, i, i].sum() == -3):
                return -1  # Player 2 wins

        # Check 3D diagonals
        if (self.board.trace() == 3 or 
            np.flipud(self.board).trace() == 3):
            return 1  # Player 1 wins
        if (self.board.trace() == -3 or 
            np.flipud(self.board).trace() == -3):
            return -1  # Player 2 wins

        return 0  # No winner yet
