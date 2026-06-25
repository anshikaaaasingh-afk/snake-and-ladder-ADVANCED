import json
import os

FILE = "data/stats.json"

class Stats:

    @staticmethod
    def load():

        if not os.path.exists(FILE):
            return {
                "games_played": 0,
                "total_rolls": 0,
                "wins": {}
            }

        with open(FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save(data):

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def add_game():

        data = Stats.load()

        data["games_played"] += 1

        Stats.save(data)

    @staticmethod
    def add_roll():

        data = Stats.load()

        data["total_rolls"] += 1

        Stats.save(data)

    @staticmethod
    def add_win(player):

        data = Stats.load()

        if player not in data["wins"]:
            data["wins"][player] = 0

        data["wins"][player] += 1

        Stats.save(data)
        