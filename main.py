from game import Game
from player import Player

from save_manager import SaveManager
from leaderboard import Leaderboard
from theme import Theme
from tournament import Tournament


def select_theme():

    print("\n===== THEMES =====")
    print("1. Classic")
    print("2. Space")
    print("3. Jungle")

    choice = input("Choose Theme: ")

    if choice == "2":
        Theme.current = "space"

    elif choice == "3":
        Theme.current = "jungle"

    else:
        Theme.current = "classic"


def create_new_game():

    game = Game()

    human_players = int(
        input(
            "\nNumber of Human Players (1-4): "
        )
    )

    for i in range(human_players):

        name = input(
            f"Player {i+1} Name: "
        )

        game.add_player(
            Player(name)
        )

    ai_players = int(
        input(
            "Number of AI Players: "
        )
    )

    for i in range(ai_players):

        game.add_player(
            Player(
                f"AI-{i+1}",
                is_ai=True
            )
        )

    return game


def load_saved_game():

    data = SaveManager.load()

    if not data:

        print("\nNo Save Found.")
        return None

    game = Game()

    for p in data:

        player = Player(
            p["name"],
            p["is_ai"]
        )

        player.position = p["position"]
        player.wins = p["wins"]

        game.add_player(player)

    print("\nSave Loaded Successfully")

    return game


def tournament_mode():

    select_theme()

    rounds = int(
        input(
            "\nTournament Rounds (1/3/5): "
        )
    )

    tournament = Tournament(rounds)

    for current_round in range(rounds):

        print(
            f"\n===== ROUND "
            f"{current_round+1} ====="
        )

        game = create_new_game()

        winner = game.play()

        tournament.add_win(
            winner.name
        )

    tournament.show()


def normal_game():

    select_theme()

    game = create_new_game()

    winner = game.play()

    print(
        f"\n🏆 Congratulations "
        f"{winner.name}"
    )


def load_game_mode():

    select_theme()

    game = load_saved_game()

    if game:

        winner = game.play()

        print(
            f"\n🏆 Congratulations "
            f"{winner.name}"
        )


def main():

    while True:

        print("\n")
        print("=" * 40)
        print(" SNAKE & LADDER PRO ")
        print("=" * 40)

        print("1. New Game")
        print("2. Load Game")
        print("3. Tournament")
        print("4. Leaderboard")
        print("5. Exit")

        choice = input(
            "\nChoose Option: "
        )

        if choice == "1":

            normal_game()

        elif choice == "2":

            load_game_mode()

        elif choice == "3":

            tournament_mode()

        elif choice == "4":

            Leaderboard.show()

        elif choice == "5":

            print("\nGoodbye!")
            break

        else:

            print(
                "\nInvalid Choice."
            )


if __name__ == "__main__":
    main()