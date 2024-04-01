import pygame
from PressureBoard import PressureBoard
import keyboard

# handles sound and music layering, volume and genres
class Sound:
    def __init__(self) -> None:
        pygame.mixer.pre_init(44100, -16, 1, 4096)
        pygame.mixer.init()

        self.selectedGenre = 0
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
        self.channels = []
        self._playAll()

    # possibly update sounds based on pressure board state
    def updateSound(self, pressureboard: PressureBoard):
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
        # loop over all channels and set volume
        pass

    def _playAll(self):
        fileNames = self.genreFiles[self.selectedGenre]
        for i, soundName in enumerate(fileNames):
            sound = pygame.mixer.Sound(soundName)
            channel =  pygame.mixer.Channel(i)
            channel.play(sound, -1)
            channel.set_volume(1)
            self.channels.append(channel)

    def _stopAll():
        pass

if __name__ == "__main__":
    sound = Sound()
    while True:
        if keyboard.is_pressed('1'):
            sound.channels[0].set_volume(0)
        if keyboard.is_pressed('2'):
            sound.channels[0].set_volume(0.5)
        if keyboard.is_pressed('3'):
            sound.channels[0].set_volume(1)