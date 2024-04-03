import Settings
from gpiozero import MCP3008
from types import SimpleNamespace

# handles inputs from 6 pressure sensors
class PressureBoard:
    def __init__(self) -> None:
        if Settings.isRaspberryPi:
            self.pressure1 = MCP3008(channel=0, device=0)
            self.pressure2 = MCP3008(channel=1, device=0)
            self.pressure3 = MCP3008(channel=2, device=0)
            self.pressure4 = MCP3008(channel=3, device=0)
            self.pressure5 = MCP3008(channel=4, device=0)
            self.pressure6 = MCP3008(channel=5, device=0)
        else:
            # if no raspberry pi is connected, simulate sensor connection
            self.pressure1 = SimpleNamespace(value=0)
            self.pressure2 = SimpleNamespace(value=0)
            self.pressure3 = SimpleNamespace(value=0)
            self.pressure4 = SimpleNamespace(value=0)
            self.pressure5 = SimpleNamespace(value=0)
            self.pressure6 = SimpleNamespace(value=0)

    # get the values 0.0-1.0 of the six sensors in a 2d array corresponding to the physical layout on the board
    def getValues(self):
        return [
            [self.pressure1.value, self.pressure2.value, self.pressure3.value], 
            [self.pressure4.value, self.pressure5.value, self.pressure6.value]
        ]

if __name__ == "__main__":
    pb = PressureBoard()
    print(pb.getValues())