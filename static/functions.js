// look way at the bottom and this main function will make sense
const main =()=> {


	// Draw the left arrow
	let canvas = document.getElementById('left_arrow');
	let ctx = canvas.getContext('2d');
	ctx.beginPath();
	ctx.moveTo(25, 50);
	ctx.lineTo(50, 25);
	ctx.lineTo(50, 75);
	ctx.fill();

	// Draw the up arrow
	canvas = document.getElementById('up_arrow');
	ctx = canvas.getContext('2d');
	ctx.beginPath();
	ctx.moveTo(50, 25);
	ctx.lineTo(25, 50);
	ctx.lineTo(75, 50);
	ctx.fill();

	// Draw the right arrow
	canvas = document.getElementById('right_arrow');
	ctx = canvas.getContext('2d');
	ctx.beginPath();
	ctx.moveTo(75, 50);
	ctx.lineTo(50, 75);
	ctx.lineTo(50, 25);
	ctx.fill();

	// Draw the down arrow
	canvas = document.getElementById('down_arrow');
	ctx = canvas.getContext('2d');
	ctx.beginPath();
	ctx.moveTo(50, 75);
	ctx.lineTo(25, 50);
	ctx.lineTo(75, 50);
	ctx.fill();


	// define the stuff that can happen
	const activate_up =(ev)=> {
		// make the border change color
		document.getElementById('up_arrow_div').style.color = 'red';

		// send the post request to turn the motor on
		let xhttp = new XMLHttpRequest();

		let url = '/activate_up';

		xhttp.open('POST', url);
		xhttp.send();
	};
	document.getElementById('up_arrow_div').addEventListener('touchstart', activate_up);
	

	const deactivate_up =()=> {
		// make the border change color
		document.getElementById('up_arrow_div').style.color = 'black';

		// send the post request to turn the motor off
		let xhttp = new XMLHttpRequest();

		let url = '/deactivate_up';

		xhttp.open('POST', url);
		xhttp.send();
	};
	document.getElementById('up_arrow_div').addEventListener('touchend', deactivate_up);


	const activate_down =()=> {
		// make the border change color
		document.getElementById('down_arrow_div').style.color = 'red';

		// send the post request to turn the motor on
		let xhttp = new XMLHttpRequest();

		let url = '/activate_down';

		xhttp.open('POST', url);
		xhttp.send();
	};
	document.getElementById('down_arrow_div').addEventListener('touchstart', activate_down);


	const deactivate_down =()=> {
		// make the border change color
		document.getElementById('down_arrow_div').style.color = 'black';

		// send the post request to turn the motor off
		let xhttp = new XMLHttpRequest();

		let url = '/deactivate_down';

		xhttp.open('POST', url);
		xhttp.send();
	};
	document.getElementById('down_arrow_div').addEventListener('touchend', deactivate_down);


	const activate_left =()=> {
		// make the border change color
		document.getElementById('left_arrow_div').style.color = 'red';

		// send the post request to move the servo left
		let xhttp = new XMLHttpRequest();

		let url = '/activate_left';

		xhttp.open('POST', url);
		xhttp.send();
	};
	document.getElementById('left_arrow_div').addEventListener('touchstart', activate_left);


	const deactivate_left =()=> {
		// make the border change color
		document.getElementById('left_arrow_div').style.color = 'black';

		// send the post request to move the servo back to neutral
		let xhttp = new XMLHttpRequest();

		let url = '/deactivate_left';

		xhttp.open('POST', url);
		xhttp.send();
	};
	document.getElementById('left_arrow_div').addEventListener('touchend', deactivate_left);


	const activate_right =()=> {
		// make the border change color
		document.getElementById('right_arrow_div').style.color = 'red';

		// send the post request to move the servo right
		let xhttp = new XMLHttpRequest();

		let url = '/activate_right';

		xhttp.open('POST', url);
		xhttp.send();
	};
	document.getElementById('right_arrow_div').addEventListener('touchstart', activate_right);


	const deactivate_right =()=> {
		// make the border change color
		document.getElementById('right_arrow_div').style.color = 'black';

		// send the post request to move the servo back to neutral
		let xhttp = new XMLHttpRequest();

		let url = '/deactivate_right';

		xhttp.open('POST', url);
		xhttp.send();
	};
	document.getElementById('right_arrow_div').addEventListener('touchend', deactivate_right);


}

// need to wait for the canvases to load before we can start
document.addEventListener('DOMContentLoaded', main)
