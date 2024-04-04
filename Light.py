from PressureBoard import PressureBoard

import json
import time
import requests

# handles lighting and communication with WLED and the ESP32
class Light:
    def __init__(self) -> None:
        self.lastUpdateTime = time.now()

    # possibly update lighting based on pressure board state
    def updateLight(self, pressureBoard: PressureBoard):
        # if time.now() == self.lastUpdateTime:
        #     return

        wled_device_ip = "192.168.12.178"
        api_endpoint = f"http://{wled_device_ip}/json/state"

        for i, value in enumerate(pressureBoard.getValues()):

        # json_data = {"on":True, "bri":0, "col":[[255,0,0]]}
        json_data = {"seg":[{"col":[[0,100,val*255]]}]}
        headers ={'content-type':'application/json'}
        r = requests.post(api_endpoint, data=json.dumps(json_data),headers=headers)
        pass

if __name__ == "__main__":
    light = Light()
    # light.updateLight()