#!/usr/bin/env pybricks-micropython

"""
75 73 75 73
"""
# Libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

import threading, math 

# Constants
WHEEL_DIAMETER = 56
AXLE_TRACK = 114

# Setup
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
left_color = ColorSensor(Port.S1)
right_color = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

# Functions