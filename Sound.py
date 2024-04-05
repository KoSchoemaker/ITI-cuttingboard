import pygame
from PressureBoard import PressureBoard
import Settings

import time
# handles sound and music layering, volume and genres
class Sound:
    def __init__(self) -> None:
        pygame.mixer.pre_init(44100, -16, 1, 4096)
        pygame.mixer.init()

        # current genre
        self.selectedGenre = 0
        # add another array in here and it counts as a different genre
        self.genreFiles = [
            [
                'music/drum.wav',
                'music/cowbell.wav',
                'music/horn.wav',
                'music/melody.wav',
                'music/guitar.wav',
                'music/synth.wav',
            ]
        ]
        # list of all the current channels
        self.channels = []
        # starting sound volume
        self.volume = 0.0
        self.soundPressureThreshold = 0.4
        self.soundPersistenceTime = 1000 #in ticks
        self.pressureBoardTimeList = [0,0,0,0,0,0]
        self._playAll()

    # possibly update sounds based on pressure board state
    def updateSound(self, pressureboard: PressureBoard):
        values = pressureboard.getValues()
        for i, value in enumerate(values):
            if self.getActivation(i, value):
                self.channels[i].set_volume(1)
            else:
                self.channels[i].set_volume(0)

        #detect change in area/pressure
        #more or less sound
        pass

    # change the genre forward
    def changeGenre(self):
        self.selectedGenre = (self.selectedGenre + 1) % len(self.genreFiles)
        self._stopAll()
        self._playAll()

    # change the volume
    def changeVolume(self, volume: int, pressureBoard: PressureBoard):
        self.volume = volume
        values = pressureBoard.getValues()
        for i, channel in enumerate(self.channels):
            if self.getActivation(i, values[i]):
                channel.set_volume(volume)

    # need to be two loops because timing is important
    def _playAll(self):
        fileNames = self.genreFiles[self.selectedGenre]

        channelList = []
        soundList = []
        for i, soundName in enumerate(fileNames):
            self.channels.append(pygame.mixer.Channel(i))
            soundList.append(pygame.mixer.Sound(soundName))

        # self.changeVolume(self.volume)
        
        for i, sound in enumerate(soundList):
            self.channels[i].play(sound, -1)

    def _stopAll(self):
        for channel in self.channels:
            channel.fadeout(1000)
        self.channels = []
        time.sleep(1.5) # ideally no sleep statements, it's blocking. But here it also serves function of blocking button readings, which is good

    # need to persist sounds for a while after threshold was reached
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
        sound.changeGenreForward()