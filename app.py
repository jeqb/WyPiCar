from car import Car
from flask import Flask

settings = {
	'motor_pin_a': 19,
	'motor_pin_b': 20,
	'motor_pin_enable': 21
}

some_car = Car(**settings)
