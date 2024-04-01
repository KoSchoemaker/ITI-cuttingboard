from PressureBoard import PressureBoard

# handles lighting and communication with WLED and the ESP32
class Light:
    def __init__(self) -> None:
        pass

    # possibly update lighting based on pressure board state
    def updateLight(self, pressureboard: PressureBoard):
        #detect change in area/pressure
        #send event to esp32
        pass