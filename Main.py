from Input import Input
import Settings
from Sound import Sound
from Light import Light
from PressureBoard import PressureBoard

import time

pressureboard = PressureBoard()
input = Input()
sound = Sound()
light = Light()

# main loop
while True:
    if input.isGenreBackward():
        sound.changeGenreBackward()

    if input.isGenreForward():
        sound.changeGenreForward()

    if input.isVolumeChanged():
        sound.changeVolume(input.volume)

    sound.updateSound(pressureboard)
    light.updateLight(pressureboard)

    # needs to be deleted later, but useful for debugging 
    time.sleep(0.3)
    print('loop')
