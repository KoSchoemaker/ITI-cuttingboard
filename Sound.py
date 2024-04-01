import pygame
from PressureBoard import PressureBoard

# handles sound and music layering, volume and genres
class Sound:
    def __init__(self) -> None:
        pass

    # possibly update sounds based on pressure board state
    def updateSound(self, pressureboard: PressureBoard):
        #detect change in area/pressure
        #more or less sound
        #play everything
        pass

    # change the genre backward
    def changeGenreBackward(self):
        pass

    # change the genre forward
    def changeGenreForward(self):
        pass

    # change the volume
    def changeVolume(self, volume: int):
        pass