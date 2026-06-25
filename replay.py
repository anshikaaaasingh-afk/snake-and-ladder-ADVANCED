import json
import time

class Replay:

    def __init__(self):
        self.moves = []

    def record(self, player, dice, position):

        self.moves.append({
            "player": player,
            "dice": dice,
            "position": position
        })

    def save(self):

        filename = f"replay_{int(time.time())}.json"

        with open(filename, "w") as f:
            json.dump(self.moves, f, indent=4)

        print(
            f"\nReplay saved as {filename}"
        )

    def play(self):

        print("\n===== REPLAY =====")

        for move in self.moves:

            print(
                f"{move['player']} rolled "
                f"{move['dice']} -> "
                f"{move['position']}"
            )
            