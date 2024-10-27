  def best_move(self):
        best_score = -float('inf')
        move = (-1, -1, -1)

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if self.board[i, j, k] == 0:
                        self.board[i, j, k] = 1
                        score = self.minimax(0, False)
                        self.board[i, j, k] = 0
                        if score > best_score:
                            best_score = score
                            move = (i, j, k)

        return move
