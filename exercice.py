#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    result = (a + b + c) / 3
    return result


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_degs += angle_mins / 60
    angle_degs += angle_secs / 3600
    result = angle_degs * math.pi / 180
    return result


def to_degrees(angle_rads: float) -> tuple:
    angle_degs = angle_rads * 180 / math.pi
    result_degs = int(angle_degs)
    angle_mins = (angle_degs - result_degs) * 60
    result_mins = int(angle_mins)
    angle_secs = (angle_mins - result_mins) * 60
    result_secs = int(angle_secs)
    return result_degs, result_mins, result_secs


def to_celsius(temperature: float) -> float:
    result = (temperature - 32) / 1.8
    return result


def to_farenheit(temperature: float) -> float:
    result = (temperature * 1.8) + 32
    return result


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
