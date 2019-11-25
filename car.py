import RPi.GPIO as GPIO
from time import sleep


class Car():
	def __init__(self, **kwargs):
		# the pins that control the motor
		self.motor_pin_a = kwargs['motor_pin_a']
		self.motor_pin_b = kwargs['motor_pin_b']
		self.motor_pin_enable = kwargs['motor_pin_enable']

		self.setup()

	def __del__(self):
		# for the garbage collector
		self.destroy()

	def setup(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.motor_pin_a, GPIO.OUT)
		GPIO.setup(self.motor_pin_b, GPIO.OUT)
		GPIO.setup(self.motor_pin_enable, GPIO.OUT)


	def destroy(self):
		GPIO.cleanup()
