import random
import time

from board import Board
from config import BOARD_SIZE

from save_manager import SaveManager
from leaderboard import Leaderboard
from achievements import Achievements
from stats import Stats
from replay import Replay

from ai import AI
from powerups import PowerUpManager
from theme import Theme
from sound import Sound


class Game:

    def __init__(self):

        self.players = []

        self.board = Board()

        self.replay = Replay()

    def add_player(self, player):

        self.players.append(player)

    def roll_dice(self):

        print("\nRolling...", end=" ")

        for _ in range(10):

            print(
                random.randint(1, 6),
                end="\r"
            )

            time.sleep(0.08)

        return random.randint(1, 6)

    def take_turn(self, player):

        print(
            f"\n===== {player.name}'s Turn ====="
        )

        print(
            f"Current Position: {player.position}"
        )

        # AI Turn
        if player.is_ai:

            dice = AI.medium(
                player.position
            )

            print(
                f"AI rolled {dice}"
            )

            time.sleep(1)

        # Human Turn
        else:

            action = input(
                "\nENTER = Roll Dice\n"
                "S = Save Game\n"
                "Choice: "
            )

            if action.lower() == "s":

                SaveManager.save(
                    self.players
                )

                print(
                    "\nGame Saved!"
                )

                return

            dice = self.roll_dice()

        Stats.add_roll()

        # Double Roll Power
        if player.double_roll:

            dice *= 2

            print(
                f"\n🔥 DOUBLE ROLL!"
            )

            print(
                f"New Roll: {dice}"
            )

            player.double_roll = False

        old_position = player.position

        player.move(dice)

        # Exact Finish Rule
        if player.position > BOARD_SIZE:

            player.position = old_position

            print(
                "\nNeed exact roll to win!"
            )

        else:

            player.position = (
                self.board.check_position(
                    player.position
                )
            )

        # Check Power-Ups
        power = (
            PowerUpManager.check(
                player.position
            )
        )

        if power:

            PowerUpManager.activate(
                player,
                power
            )

            if power == "EXTRA_TURN":

                player.extra_turn = True

            elif power == "DOUBLE_ROLL":

                player.double_roll = True

        # Replay Recording
        self.replay.record(
            player.name,
            dice,
            player.position
        )

        print(
            f"\n{player.name} moved to "
            f"{player.position}"
        )

        # Extra Turn Power
        if player.extra_turn:

            print(
                f"\n⚡ {player.name}"
                " gets an EXTRA TURN!"
            )

            player.extra_turn = False

            self.take_turn(player)

    def process_winner(
        self,
        player
    ):

        Sound.win()

        print(
            Theme.color(
                "win",
                f"\n🏆 "
                f"{player.name} WINS!"
            )
        )

        # Statistics
        Stats.add_game()

        Stats.add_win(
            player.name
        )

        # Leaderboard
        Leaderboard.update(
            player.name
        )

        # Achievements
        Achievements.unlock(
            player.name,
            "First Victory"
        )

        if player.position == 100:

            Achievements.unlock(
                player.name,
                "Perfect Finish"
            )

        # Replay Save
        self.replay.save()

    def play(self):

        print(
            "\n🎲 GAME STARTED 🎲"
        )

        while True:

            self.board.display(
                self.players
            )

            for player in self.players:

                self.take_turn(
                    player
                )

                if (
                    player.position
                    == BOARD_SIZE
                ):

                    player.wins += 1

                    self.process_winner(
                        player
                    )

                    return player