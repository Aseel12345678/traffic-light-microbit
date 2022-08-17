#Download libraries from these two links
#https://github.com/MeqdadDev/microbit-micropython-samples/blob/main/External%20Components%20with%20microbit/OLED%20Screen/ssd1306.py
#https://github.com/MeqdadDev/microbit-micropython-samples/blob/main/External%20Components%20with%20microbit/OLED%20Screen/ssd1306_text.py

from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
initialize()
clear_oled()

while True:
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    add_text(0, 0, "Go")
    sleep(4000)
    clear_oled()

    pin0.write_digital(0)
    pin1.write_digital(1)
    add_text(0, 0, "Slow Down")
    add_text(0, 1, "And Be Ready...")
    sleep(2000)
    clear_oled()
    
    pin1.write_digital(0)
    pin2.write_digital(1)
    add_text(0, 0, "Stop")
    sleep(4000)
    clear_oled()
    
    pin2.write_digital(0)
    pin1.write_digital(1)
    add_text(0, 0, "Be Ready...")
    sleep(2000)
    clear_oled()





