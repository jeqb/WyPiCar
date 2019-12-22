import time

from car import Car
from flask import Flask

# remember -> GPIO.setmode(GPIO.BCM)
settings = {
	'motor_pin_a': 19,
	'motor_pin_b': 20,
	'motor_pin_enable': 21,
	'servo_pin': 18
}

some_car = Car(**settings)

try:
	some_car.turn_motor_on()
	time.sleep(2)
	some_car.set_motor_direction_backwards()
	time.sleep(2)
	some_car.turn_motor_off()
	"""
	time.sleep(2)
	some_car.move_servo_to(0)
	time.sleep(2)
	some_car.move_servo_to(90)
	time.sleep(2)
	some_car.move_servo_to(0)
	time.sleep(2)
	"""
except:
	del some_car
	