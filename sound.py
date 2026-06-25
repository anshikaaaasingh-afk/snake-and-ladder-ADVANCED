import os

class Sound:

    @staticmethod
    def snake():
        os.system("afplay /System/Library/Sounds/Funk.aiff")

    @staticmethod
    def ladder():
        os.system("afplay /System/Library/Sounds/Glass.aiff")

    @staticmethod
    def win():
        os.system("afplay /System/Library/Sounds/Hero.aiff")