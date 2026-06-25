from colorama import Fore, Style, init

init(autoreset=True)

class Theme:

    THEMES = {
        "classic": {
            "snake": Fore.RED,
            "ladder": Fore.GREEN,
            "win": Fore.YELLOW
        },

        "space": {
            "snake": Fore.MAGENTA,
            "ladder": Fore.CYAN,
            "win": Fore.WHITE
        },

        "jungle": {
            "snake": Fore.GREEN,
            "ladder": Fore.YELLOW,
            "win": Fore.CYAN
        }
    }

    current = "classic"

    @classmethod
    def color(cls, category, text):

        return (
            cls.THEMES[cls.current][category]
            + text
            + Style.RESET_ALL
        )