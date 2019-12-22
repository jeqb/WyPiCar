from flask import Flask, render_template

# from car import Car

app = Flask(__name__, static_url_path='/static')


# "UI" sent to client
@app.route('/')
def car_controller():

	return render_template('CarController.html')

# push up arrow
@app.route('/activate_up', methods = ['POST'])
def activate_up():
	# do car stuff here
	return '', 200

# release up arrow
@app.route('/deactivate_up', methods = ['POST'])
def deactivate_up():
	# do car stuff here
	return '', 200

# push down arrow
@app.route('/activate_down', methods = ['POST'])
def activate_down():
	# do car stuff here
	return '', 200

# release down arrow
@app.route('/deactivate_down', methods = ['POST'])
def deactivate_down():
	# do car stuff here
	return '', 200

# push left arrow
@app.route('/activate_left', methods = ['POST'])
def activate_left():
	# do car stuff here
	return '', 200

# release left arrow
@app.route('/deactivate_left', methods = ['POST'])
def deactivate_left():
	# do car stuff here
	return '', 200

# push right arrow
@app.route('/activate_right', methods = ['POST'])
def activate_right():
	# do car stuff here
	return '', 200

# release right arrow
@app.route('/deactivate_right', methods = ['POST'])
def deactivate_right():
	# do car stuff here
	return '', 200


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
	