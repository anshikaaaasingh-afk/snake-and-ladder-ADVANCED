import random

class AI:

    @staticmethod
    def easy():
        return random.randint(1,6)

    @staticmethod
    def medium(position):

        if position >= 94:
            return 100 - position

        return random.randint(1,6)

    @staticmethod
    def hard(position):

        target = 100 - position

        if 1 <= target <= 6:
            return target

        return random.randint(1,6)
    