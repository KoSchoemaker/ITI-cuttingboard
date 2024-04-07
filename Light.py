from PressureBoard import PressureBoard
from gpiozero import PWMLED

import json
import time
import requests

# handles lighting and communication with WLED and the ESP32
class Light:
    def __init__(self) -> None:
        self.updateHowManyTicks = 100
        self.currentTick = 0

    # possibly update lighting based on pressure board state
    def updateLight(self, pressureBoard: PressureBoard):
        if self.updateHowManyTicks >= self.currentTick:
            self.currentTick = self.currentTick + 1
            return
        self.currentTick = 0
        
        r, g, b = 0, 0, 0
        values = pressureBoard.getValues()
        
        if len(values) >= 3:
            r = values[0] * 255
            g = values[1] * 255
            b = values[2] * 255
            
        brightness = max(values)

        # for i, value in enumerate(pressureBoard.getValues()):
        #     if i == 1:
        #         r = value * 255
        #     if i == 2:
        #         g = value * 255
        #     if i == 3:
        #         b = value * 255
        
        
        # json_data = {"on":True, "bri":0, "col":[[255,0,0]]}
        json_data = {"seg":[{"col":[[r, g, b]], "bri": int(brightness * 255)}]}

        device = "192.168.12.178"
        endpoint = f"http://{device}/json/state"
        headers ={'content-type':'application/json'}
        try:
            requests.post(endpoint, data=json.dumps(json_data),headers=headers, timeout=1)
        except Exception as e:
            print(e)
            pass
        
if __name__ == "__main__":
    light = Light()
    while True:
        light.updateLight()
        # time.sleep(0.1)