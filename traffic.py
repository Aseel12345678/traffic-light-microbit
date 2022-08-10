from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
initialize()
clear_oled()

sleep(1000)

while True:
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    add_text(0, 0, "Go")
    sleep(4000)
    pin0.write_digital(0)
    pin1.write_digital(1)
    add_text(0, 0, "Slow down")
    add_text(0, 1, "And be ready")
    sleep(2000)
    pin1.write_digital(0)
    pin2.write_digital(1)
    add_text(0, 0, "Stop")
    sleep(4000)
     pin0.write_digital(0)
    pin1.write_digital(1)
    add_text(0, 0, "Slow down")
    add_text(0, 1, "And be ready")
    sleep(2000)
