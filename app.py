import json

from flask import Flask, render_template

from car import Car


# load configuration settings for the car object and then instantiate
with open('configuration.json', 'r') as json_file:
	settings = json.load(json_file)

some_car = Car(**settings)


app = Flask(__name__, static_url_path='/static')


# "UI" sent to client
@app.route('/')
def car_controller():

	return render_template('CarController.html')


# push up arrow
@app.route('/activate_up', methods = ['POST'])
def activate_up():

	some_car.set_motor_direction_forward()
	some_car.turn_motor_on()

	return '', 200


# release up arrow
@app.route('/deactivate_up', methods = ['POST'])
def deactivate_up():

	some_car.turn_motor_off()

	return '', 200


# push down arrow
@app.route('/activate_down', methods = ['POST'])
def activate_down():

	some_car.set_motor_direction_backwards()
	some_car.turn_motor_on()

	return '', 200


# release down arrow
@app.route('/deactivate_down', methods = ['POST'])
def deactivate_down():

	some_car.turn_motor_off()

	return '', 200


# push left arrow
@app.route('/activate_left', methods = ['POST'])
def activate_left():

	some_car.move_servo_to(45)

	return '', 200


# release left arrow
@app.route('/deactivate_left', methods = ['POST'])
def deactivate_left():

	some_car.move_servo_to(90)

	return '', 200


# push right arrow
@app.route('/activate_right', methods = ['POST'])
def activate_right():

	some_car.move_servo_to(135)

	return '', 200


# release right arrow
@app.route('/deactivate_right', methods = ['POST'])
def deactivate_right():

	some_car.move_servo_to(90)

	return '', 200


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', use_reloader=False)
