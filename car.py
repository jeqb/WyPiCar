# import RPi.GPIO as GPIO
# from time import sleep

# pins to control the motor
motorA = 19
motorb = 20
motorEnable = 21

class Car():
	def __init__(self, **kwargs):
		# the pins that control the motor
		self.motor_pin_a = kwargs['motor_pin_a']
		self.motor_pin_b = kwargs['motor_pin_b']
		self.motor_pin_enable = kwargs['motor_pin_enable']

if __name__ == '__main__':
	some_car = Car()
