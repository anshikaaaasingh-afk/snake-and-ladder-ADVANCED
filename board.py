from config import SNAKES, LADDERS
from theme import Theme
from sound import Sound


class Board:

    def __init__(self):
        pass

    def check_position(self, position):

        # Snake
        if position in SNAKES:

            Sound.snake()

            print(
                Theme.color(
                    "snake",
                    f"\n🐍 Snake! "
                    f"{position} -> "
                    f"{SNAKES[position]}"
                )
            )

            return SNAKES[position]

        # Ladder
        if position in LADDERS:

            Sound.ladder()

            print(
                Theme.color(
                    "ladder",
                    f"\n🪜 Ladder! "
                    f"{position} -> "
                    f"{LADDERS[position]}"
                )
            )

            return LADDERS[position]

        return position

    def display(self, players):

        print("\n")
        print("=" * 90)
        print(" " * 30 + "SNAKE & LADDER BOARD")
        print("=" * 90)

        for row in range(10, 0, -1):

            start = (row - 1) * 10 + 1
            end = row * 10

            numbers = list(
                range(start, end + 1)
            )

            # Zig-zag board pattern
            if row % 2 == 0:
                numbers.reverse()

            line = ""

            for num in numbers:

                markers = []

                for player in players:

                    if player.position == num:

                        markers.append(
                            player.name[0].upper()
                        )

                if markers:

                    marker_text = "".join(markers)

                    cell = (
                        f"[{marker_text}]"
                    )

                else:

                    cell = (
                        f"{num:02}"
                    )

                line += (
                    f"{cell:^8}"
                )

            print(line)

        print("=" * 90)

        print("\nPLAYER POSITIONS")

        for player in players:

            print(
                f"{player.name:<15}"
                f"-> "
                f"{player.position}"
            )

        print()