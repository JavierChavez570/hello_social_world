import serial
arduino = serial.Serial('/dev/cu.usbmodem1411', 115200, timeout=.1)
while True:
	referencia = arduino.readline()
	if referencia == 1000:
		print referencia
		pass
	print referencia
	pass
arduino.close()