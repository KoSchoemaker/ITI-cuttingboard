from PressureBoard import PressureBoard

import json
import time
import requests

# handles lighting and communication with WLED and the ESP32
class Light:
    def __init__(self) -> None:
        self.updateHowManyTicks = 10000
        self.currentTick = 0

    # possibly update lighting based on pressure board state
    def updateLight(self, pressureBoard: PressureBoard):
        if self.updateHowManyTicks >= self.currentTick:
            self.currentTick = self.currentTick + 1
            return
        self.currentTick = 0

        for i, value in enumerate(pressureBoard.getValues()):
            if i == 1:
                r = value * 255
            if i == 2:
                g = value * 255
            if i == 3:
                b = value * 255
        
        # json_data = {"on":True, "bri":0, "col":[[255,0,0]]}
        json_data = {"seg":[{"col":[[r, g, b]]}]}

        device = "192.168.12.178"
        endpoint = f"http://{device}/json/state"
        headers ={'content-type':'application/json'}
        try:
            requests.post(endpoint, data=json.dumps(json_data),headers=headers, timeout=1)
        except Exception as e:
            # print(e)
            pass

if __name__ == "__main__":
    light = Light()
    # light.updateLight()