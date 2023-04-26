#!/usr/bin/env python
# coding=utf-8

import tm1637
from time import sleep

# Initialize the display
display = tm1637.TM1637(clk=23, dio=24)


# Define a scrolling message
display.scroll("**Love You**", 500)
sleep(2)
display.scroll("Hello World This is a scrolling marquee", 500)
sleep(2)

# Clear the display when finished
display.show('bye')


