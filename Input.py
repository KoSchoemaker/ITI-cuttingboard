import Settings

from types import SimpleNamespace
from gpiozero import MCP3008, Button

# handeling inputs that are not pressure sensors: buttons and knobs
class Input:
    def __init__(self) -> None:
        if Settings.isRaspberryPi:
            self.volumeControl = MCP3008(channel=1, device=0)
            self.lightControl = MCP3008(channel=7, device=0)
            self.genreForward = Button(15)
            self.genreBackward = Button(5)
        else:
            # if no raspberry pi is connected, simulate sensor connection
            self.volumeControl = SimpleNamespace(value=0)
            self.lightControl = SimpleNamespace(value=0)
            self.genreForward = SimpleNamespace(isPressed=False)
            self.genreBackward = SimpleNamespace(isPressed=False)
        self.volume = 0.0
        self.lightIntensity = 0.0
        self.volumeThreshold = 0.1

    # get current value from an analogue sensor
    def getValue(sensor: MCP3008):
        return sensor.value

    # True/False sense if the genre forward button is pressed. Only the moment when pressed does this return True
    def isGenreForward(self):
        return self.genreForward.isPressed

    # True/False sense if the genre backward button is pressed. Only the moment when pressed does this return True
    def isGenreBackward(self):
        return self.genreBackward.isPressed

    # calculate if volume is changed based on previous volume. This is needed because potentiometer flucutates a lot
    # and raw sensor value cannot really be trusted
    def calculateVolume(self):
        pass

    # True/False if volume was changed, based on calculateVolume() above
    def isVolumeChanged(self):
        value = self.volumeControl.value
        abs(value - self.volume) > self.volumeThreshold
        self.volume = value

    # get the volume, based on calculateVolume()
    def getVolume(self):
        return self.volume
    
    # calculate if light intensity is changed based on previous value. This is needed because potentiometer flucutates a lot
    # and raw sensor value cannot really be trusted
    def calculateLightIntensity(self):
        pass

    # True/False if light intensity was changed, based on calculateLightIntensity() above
    def isLightChanged():
        pass

    # get the volume, based on calculateLightIntensity()
    def getLightIntensity(self):
        return self.lightIntensity