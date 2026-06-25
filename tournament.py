class Tournament:

    def __init__(self, rounds):

        self.rounds = rounds

        self.scoreboard = {}

    def add_win(self, player):

        if player not in self.scoreboard:
            self.scoreboard[player] = 0

        self.scoreboard[player] += 1

    def show(self):

        print("\n===== TOURNAMENT =====")

        for p, score in self.scoreboard.items():

            print(
                f"{p}: {score}"
            )
            