README for Margo Sikes project.py:

Arduino required to run the project; utilizes two potentiometers and an accelerometer.
	It also requires users to install PySerial to allow communication between Arduino + Python.
	PySerial: https://pythonhosted.org/pyserial/pyserial.html#installation

NOTE: Confirm that the Arduino is plugged into COM3 using the Arduino software--if it is a different
	port, update line 133 to the new port.

To draw:
	The left potentiometer will increase the speed of the pen from 0 to 3.
	The right potentiometer will change the angle of the pen and will move pen left
		or right depending on its heading.

To clear:
	Shake the arduino repeatedly until the drawing disappears.

NOTE: it is recommended to turn the pen speed down to 0 before clearing so it
	does not keep drawing.