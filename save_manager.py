import json
import os

SAVE_FILE = "saves/savegame.json"

class SaveManager:

    @staticmethod
    def save(players):

        data = []

        for p in players:
            data.append({
                "name": p.name,
                "position": p.position,
                "wins": p.wins,
                "is_ai": p.is_ai
            })

        with open(SAVE_FILE, "w") as f:
            json.dump(data, f, indent=4)

        print("Game Saved")

    @staticmethod
    def load():

        if not os.path.exists(SAVE_FILE):
            return None

        with open(SAVE_FILE, "r") as f:
            return json.load(f)