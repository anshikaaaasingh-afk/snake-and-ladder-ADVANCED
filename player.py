class Player:

    def __init__(self, name, is_ai=False):

        self.name = name
        self.position = 0
        self.wins = 0
        self.is_ai = is_ai

        # Power-up attributes
        self.shield = False
        self.extra_turn = False
        self.double_roll = False

    def move(self, dice):

        self.position += dice

    def reset(self):

        self.position = 0

    def __str__(self):

        return f"{self.name} ({self.position})"