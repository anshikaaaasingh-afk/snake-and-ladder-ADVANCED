import random

POWERUPS = {
    15: "EXTRA_TURN",
    35: "DOUBLE_ROLL",
    75: "SHIELD"
}

class PowerUpManager:

    @staticmethod
    def check(position):

        return POWERUPS.get(position)

    @staticmethod
    def activate(player, power):

        print(
            f"\n⚡ {player.name} got {power}"
        )

        if power == "SHIELD":
            player.shield = True

        return power
    