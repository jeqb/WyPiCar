import RPi.GPIO as GPIO
import time


class Car():
	def __init__(self, **kwargs):
		# the pins that control the motor
		self.motor_pin_a = kwargs['motor_pin_a']
		self.motor_pin_b = kwargs['motor_pin_b']
		self.motor_pin_enable = kwargs['motor_pin_enable']

		# define parameters that the servo operates on
		# if None provided, defaults to values on right of or
		self.servo_pin = kwargs['servo_pin']
		self.servo_offset_error = kwargs.get('servo_offset_error') or 0.5
		self.servo_min_duty = (
								(kwargs.get('servo_min_duty') or  2.5)
								+ self.servo_offset_error
								)
		self.servo_max_duty = (
								(kwargs.get('servo_max_duty') or 12.5)
								+ self.servo_offset_error
								)

		self.setup()
		self.set_motor_direction_forward()


	# for the garbage collector
	def __del__(self):
		self.destroy()


	def setup(self):
		GPIO.setmode(GPIO.BCM)

		# motor
		GPIO.setup(self.motor_pin_a, GPIO.OUT)
		GPIO.setup(self.motor_pin_b, GPIO.OUT)
		GPIO.setup(self.motor_pin_enable, GPIO.OUT)

		# servo
		GPIO.setup(self.servo_pin, GPIO.OUT)
		GPIO.output(self.servo_pin, GPIO.LOW)
		global servo_pulse
		servo_pulse = GPIO.PWM(self.servo_pin, 50)
		servo_pulse.start(0)


	# servo methods
	def map(self, value, from_low, from_high, to_low, to_high):
		return (to_high - to_low)*(value - from_low) / (from_high - from_low) + to_low


	def move_servo_to(self, angle):
		# ensure angles stay within the bounds of reason
		if angle < 0:
			angle = 0
		elif angle > 180:
			angle = 180

		# map the angle to the duty cycle and assign it to the servo_pulse
		assignment = self.map(angle, 0, 180, self.servo_min_duty, self.servo_max_duty)
		servo_pulse.ChangeDutyCycle(assignment)


	# motor methods
	def turn_motor_on(self):
		GPIO.output(self.motor_pin_enable, GPIO.HIGH)


	def turn_motor_off(self):
		GPIO.output(self.motor_pin_enable, GPIO.LOW)


	def set_motor_direction_forward(self):
		GPIO.output(self.motor_pin_a, GPIO.HIGH)
		GPIO.output(self.motor_pin_b, GPIO.LOW)


	def set_motor_direction_backwards(self):
		GPIO.output(self.motor_pin_b, GPIO.HIGH)
		GPIO.output(self.motor_pin_a, GPIO.LOW)


	# clean up resources
	def destroy(self):
		servo_pulse.stop()
		GPIO.cleanup()

