def print_board(self):
        for z in range(3):
            print(f"Layer {z + 1}:")
            print(self.board[:, :, z])
            print()
