def minimax(self, depth, is_maximizing):
        score = self.check_winner()
        if score != 0:
            return score

        if np.all(self.board != 0):
            return 0  # Draw

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        if self.board[i, j, k] == 0:
                            self.board[i, j, k] = 1
                            score = self.minimax(depth + 1, False)
                            self.board[i, j, k] = 0
                            best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        if self.board[i, j, k] == 0:
                            self.board[i, j, k] = -1
                            score = self.minimax(depth + 1, True)
                            self.board[i, j, k] = 0
                            best_score = min(best_score, score)
            return best_score
