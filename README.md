# ITI-cuttingboard

Codebase for the ✨Slice of Magic Cuttingboard✨, made by the 🐕Golden Retrievers🐕 

This code is made to run on Raspberry Pi, but can be executed on other devices as well, although sensor inputs and light events will not work then.

- **Main.py**: main file containing while loop, calling all other functionality from here
- **PressureBoard.py**: functionality concerning pressure sensors
- **Input.py**: functionality concerning other sensor input besides pressure: 2 genre buttons, light intensity potentiometer, sound volume potentiometer
- **Sound.py**: functionality concerning playing sound(s), layering sounds, volume, beat etc.
- **Light.py**: functionality concerning lighting and communitation with WLED and the ESP32
- **Settings.py**: general settings or defines needed over multiple files.