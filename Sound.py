import pygame
from PressureBoard import PressureBoard

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
        self.volume = 1.0
        self._playAll()

    # possibly update sounds based on pressure board state
    def updateSound(self, pressureboard: PressureBoard):
        values = pressureboard.getValues()
        first = values[0][2]
        if first > 0.3:
            self.channels[0].set_volume(0)
            self.channels[4].set_volume(0)
        else:
            self.channels[0].set_volume(1)
            self.channels[4].set_volume(1)
        #detect change in area/pressure
        #more or less sound
        pass

    # change the genre backward
    def changeGenreBackward(self):
        self.selectedGenre = (self.selectedGenre - 1) % len(self.genreFiles)
        self._stopAll()
        self._playAll()

    # change the genre forward
    def changeGenreForward(self):
        self.selectedGenre = (self.selectedGenre + 1) % len(self.genreFiles)
        self._stopAll()
        self._playAll()

    # change the volume
    def changeVolume(self, volume: int):
        self.volume = volume
        for channel in self.channels:
            if channel.get_volume() > 0.1:
                channel.set_volume(volume)

    # need to be two loops because timing is important
    def _playAll(self):
        fileNames = self.genreFiles[self.selectedGenre]

        channelList = []
        soundList = []
        for i, soundName in enumerate(fileNames):
            self.channels.append(pygame.mixer.Channel(i))
            soundList.append(pygame.mixer.Sound(soundName))

        for i, sound in enumerate(soundList):
            self.channels[i].play(sound, -1)

    def _stopAll(self):
        for channel in self.channels:
            channel.fadeout(1000)
        self.channels = []
        time.sleep(1.5) # ideally no sleep statements, it's blocking. But here it also serves function of blocking button readings, which is good

if __name__ == "__main__":
    sound = Sound()
    while True:
        time.sleep(8)
        sound.changeGenreForward()