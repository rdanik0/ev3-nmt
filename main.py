#!/usr/bin/env pybricks-micropython

"""
75 73 75 73
"""
# Библиотеки
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

import threading, math 

# Константы
WHEEL_DIAMETER = 56
AXLE_TRACK = 114

# Инициализация
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
left_color_sensor = ColorSensor(Port.S1)
right_color_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)

# Структура Сенсоров
class ColorSensorData:
    def __init__(self, name):
        self.name = name
        self.R = 0
        self.G = 0
        self.B = 0
        self.brightness = 0

    def update(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B
        self.brightness = (R + G + B) / 3

    def is_white(self, threshold=50):
        return self.brightness > threshold

    def is_black(self, threshold=50):
        return self.brightness < threshold
    
    def is_green(self, threshold=1.5):
        # Если уровень зеленого в полтора раза лидирует над красным и синим, делаем вывод что это зеленый
        return self.G > self.R * threshold and self.G > self.B * threshold

left_color = ColorSensorData("Left")
right_color = ColorSensorData("Right")
# Функции ()
def line_seeker():
    while True:
        # Вперед
        if left_color.is_white() and right_color.is_white():
            print("Forward")

        # Вправо
        elif left_color.is_white() and right_color.is_black():
            print("Right")

        # Влево
        elif left_color.is_black() and right_color.is_white():
            print("Left")

def green_seeker():
    while True:
        # Зеленый с обеих сторон
        if left_color.is_green() and right_color.is_green():
            print("Turn 180")
        
        # Зеленый слева
        elif left_color.is_green():
            print("Turn 90")
        
        # Зеленый справа
        elif right_color.is_green():
            print("Turn -90")

def main():
    # Запуск потоков
    line_thread = threading.Thread(target=line_seeker)
    green_thread = threading.Thread(target=green_seeker)

    line_thread.start()
    green_thread.start()

    # Обновление данных сенсоров
    while True:
        left_color.update(*left_color_sensor.rgb())
        right_color.update(*right_color_sensor.rgb())