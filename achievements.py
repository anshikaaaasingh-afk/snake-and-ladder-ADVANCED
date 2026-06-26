import json
import os

FILE = "data/achievements.json"

class Achievements:

    @staticmethod
    def load():

        if not os.path.exists(FILE):
            return {}

        with open(FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def unlock(player, achievement):

        data = Achievements.load()

        if player not in data:
            data[player] = []

        if achievement not in data[player]:

            data[player].append(achievement)
            

            print(
                f"\n🏅 Achievement Unlocked: {achievement}"
            )

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def show(player):

        data = Achievements.load()

        print("\nAchievements")

        for a in data.get(player, []):
            print("-", a)
            
