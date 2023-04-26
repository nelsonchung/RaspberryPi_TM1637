#!/usr/bin/env python
# coding=utf-8

import tm1637
from time import sleep

# Initialize the display
display = tm1637.TM1637(clk=23, dio=24)

# all LEDS off
display.write([0, 0, 0, 0])
sleep(0.1)

# all LEDS on "88:88"
display.write([127, 255, 127, 127])
sleep(2)

# show "0123"
#display.write([63, 6, 91, 79])
#sleep(2)
display.number(0)
sleep(1)
display.number(12)
sleep(1)
display.number(123)
sleep(1)
display.number(1234)
sleep(1)
display.scroll("1234567890", 500)
sleep(1)


# Set the brightness (0-7)
display.brightness(3)

# show "Help"
display.show('help')
sleep(2)

# Define a scrolling message
display.scroll("**Love You**", 500)
sleep(2)
display.scroll("Hello World This is a scrolling marquee", 500)
sleep(2)

# Clear the display when finished
display.show('bye')


