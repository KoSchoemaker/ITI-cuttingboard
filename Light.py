from PressureBoard import PressureBoard
from gpiozero import PWMLED

import json
import time
import requests

# handles lighting and communication with WLED and the ESP32
class Light:
    def __init__(self) -> None:
        self.updateHowManyTicks = 10
        self.currentTick = 0
        self.multiplyer = 200
        self.brightnessMultiplyer = 18

    # possibly update lighting based on pressure board state
    def updateLight(self, pressureBoard: PressureBoard, lightIntensity: float):
        if self.updateHowManyTicks >= self.currentTick:
            self.currentTick = self.currentTick + 1
            return
        self.currentTick = 0
        
        r, g, b = 0, 0, 0
        values = pressureBoard.getValues()

        multiplyer = self.multiplyer
        if len(values) >= 6:
            r = min(values[0] * multiplyer + values[3] * multiplyer, 255)
            g = min(values[1] * multiplyer + values[4] * multiplyer, 255)
            b = min(values[2] * multiplyer + values[5] * multiplyer, 255)
            
        brightness = int(min(max(max(values) * self.brightnessMultiplyer - (1 - lightIntensity) * 15, 0), 255))

        # jsonData = {"on":True, "bri":255, "col":[[255,0,0]]}
        jsonData = {"seg":[{"col":[[int(r), int(g), int(b)]], "bri": brightness}]}

        device = "192.168.12.178"
        endpoint = f"http://{device}/json/state"
        headers ={'content-type':'application/json'}
        try:
            requests.post(endpoint, data=json.dumps(jsonData),headers=headers, timeout=1)
        except Exception as e:
            print(e)
            pass
        
if __name__ == "__main__":
    light = Light()
    while True:
        light.updateLight()
        # time.sleep(0.1)