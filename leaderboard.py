import json
import os

FILE = "data/leaderboard.json"

class Leaderboard:

    @staticmethod
    def load():

        if not os.path.exists(FILE):
            return {}

        with open(FILE,
"r") as f:
            return json.load(f)

    @staticmethod
    def update(player):

        board = Leaderboard.load()

        if player not in board:
            board[player
] = 0

        board[player
] += 1

        with open(FILE,
"w") as f:
            json.dump(board, f, indent=4)

    @staticmethod
    def show():

        board = Leaderboard.load()

        print("\n===== LEADERBOARD =====")

        sorted_board = sorted(
            board.items(),
            key=lambda x: x[
    1
],
            reverse=True
        )

        for rank, (name, wins) in enumerate(sorted_board, start=1):
            print(f"{rank}. {name} - {wins} wins")