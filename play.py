   def play_game(self):
        while True:
            self.print_board()
            if self.current_player == 1:  # Player 1's turn
                x, y, z = map(int, input("Enter your move (x y z): ").split())
                if self.board[x, y, z] == 0:
                    self.board[x, y, z] = 1
                    self.current_player = -1
                else:
                    print("Invalid move. Try again.")
            else:  # Computer's turn
                move = self.best_move()
                if move != (-1, -1, -1):
                    self.board[move] = -1
                self.current_player = 1

            winner = self.check_winner()
            if winner != 0:
                self.print_board()
                if winner == 1:
                    print("Player 1 wins!")
                else:
                    print("Player 2 (Computer) wins!")
                break
            elif np.all(self.board != 0):
                self.print_board()
                print("It's a draw!")
                break

if __name__ == "__main__":
    game = TicTacToe3D()
    game.play_game()
