import time

# from car import Car
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def car_controller():

	return render_template('CarController.html')

if __name__ == '__main__':
	app.run(debug=True)
	