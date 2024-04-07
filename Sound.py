import pygame
from PressureBoard import PressureBoard

import time

# handles sound and music layering, volume and genres
class Sound:
    def __init__(self) -> None:
        pygame.mixer.pre_init(44100, -16, 1, 4096)
        pygame.mixer.init()

        self.selectedGenre = 0                      # currently selected genre
        self.genreFiles = [                         # add another array in here and it counts as a different genre
            [
                'music/drum.wav',
                'music/cowbell.wav',
                'music/horn.wav',
                'music/melody.wav',
                'music/guitar.wav',
                'music/synth.wav',
            ],
            [
                'music/Hand clap.wav',
                'music/High Q 3.wav',
                'music/Kick drum.wav',
                'music/Mid tom.wav',
                'music/Piano.wav',
                'music/Sticks.wav'
            ]
        ]
        self.channels = []                          # list of all the current channels
        self.volume = 0.0                           # starting sound volume
        self.soundPressureThreshold = 0.4           # how much pressure applied before sound starts playing
        self.soundPersistenceTime = 1000            # how much longer does the music play after activation has ended, in ticks
        self.pressureBoardTimeList = [0,0,0,0,0,0]  # activation list, in ticks
        self._playAll()

    # possibly update sounds based on pressure board state
    def updateSound(self, pressureboard: PressureBoard):
        values = pressureboard.getValues()
        for i, value in enumerate(values):
            if self.getActivation(i, value):
                self.channels[i].set_volume(self.volume)
            else:
                self.channels[i].set_volume(0)

    # change the genre forward
    def changeGenre(self):
        self.selectedGenre = (self.selectedGenre + 1) % len(self.genreFiles)
        self._stopAll()
        self._playAll()

    # change the volume
    def changeVolume(self, pressureBoard: PressureBoard, volume: float):
        self.volume = volume
        values = pressureBoard.getValues()
        for i, channel in enumerate(self.channels):
            if self.getActivation(i, values[i]):
                channel.set_volume(volume)

    # need to be two loops because timing is important
    def _playAll(self):
        fileNames = self.genreFiles[self.selectedGenre]

        soundList = []
        for i, soundName in enumerate(fileNames):
            channel = pygame.mixer.Channel(i)
            channel.set_volume(self.volume)
            self.channels.append(channel)
            soundList.append(pygame.mixer.Sound(soundName))

        for i, sound in enumerate(soundList):
            self.channels[i].play(sound, -1)

    def _stopAll(self):
        for channel in self.channels:
            channel.fadeout(1000)
        self.channels = []
        time.sleep(1.5) # ideally no sleep statements, it's blocking. But here it also serves function of blocking button readings, which is good

    # need to persist sounds for a while after threshold was reached. Activation list saves how long should go on for.
    def getActivation(self, index, value):
        previousBoardTime = self.pressureBoardTimeList[index]

        if value > self.soundPressureThreshold and previousBoardTime != self.soundPersistenceTime:
            boardTime = self.soundPersistenceTime
        elif previousBoardTime <= 0:
            return False
        else:
            boardTime = previousBoardTime - 1
        self.pressureBoardTimeList[index] = boardTime
        return True

if __name__ == "__main__":
    sound = Sound()
    while True:
        time.sleep(8)
        sound.changeGenre()