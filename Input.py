import Settings
import time
from types import SimpleNamespace
from gpiozero import MCP3008, Button

# handeling inputs that are not pressure sensors: buttons and knobs
class Input:
    def __init__(self) -> None:
        if Settings.isRaspberryPi:
            self.volumeControl = MCP3008(channel=6, device=0)
            self.lightControl = MCP3008(channel=0, device=0)
            self.genreControl = Button(2)
        else:
            # if no raspberry pi is connected, simulate sensor connection
            self.volumeControl = SimpleNamespace(value=1)
            self.lightControl = SimpleNamespace(value=1)
            self.genreControl = SimpleNamespace(is_pressed=False)
        self.volume = 0.0
        self.volumeThreshold = 0.05

    # True/False sense if the genre button is pressed. Only the moment when pressed does this return True
    def isGenreChanged(self):
        return self.genreControl.is_pressed

    # True/False if volume was changed, based on calculateVolume() above
    def isVolumeChanged(self):
        value = self.volumeControl.value
        changed = abs(value - self.volume) > self.volumeThreshold
        if changed:
            self.volume = value
        return changed
    
if __name__ == "__main__":
    pb = Input()
    while True:
        print(pb.genreControl.is_pressed)
        # time.sleep(1)
    # print(pb.getAveragePressureBoard())