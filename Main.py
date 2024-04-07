from Input import Input
from Sound import Sound
from Light import Light
from PressureBoard import PressureBoard

# init
pressureboard = PressureBoard()
input = Input()
sound = Sound()
light = Light()

sound.volume = input.volumeControl.value    # init the sound volume, set to the knob value

# main loop
while True:
    pressureboard.loadValues()  # request new values from the pressure sensors for this tick
    if input.isGenreChanged():  # change genre if genre button is pushed
        sound.changeGenre()

    if input.isVolumeChanged(): # change sound volume if volume knob is turned more than input.volumeThreshold
        sound.changeVolume(pressureboard, input.volume) # needs pressureboard because only activated sounds should have volume changed

    sound.updateSound(pressureboard)                                # update sound based on pressure input
    light.updateLight(pressureboard, input.lightControl.value)      # update light based on pressure input and light control