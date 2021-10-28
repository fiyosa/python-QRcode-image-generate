from serial import Serial

class usb_port:
	def __init__(self, start, stop, port, loop):
		self.start = start.strip()
		self.stop  = stop.strip()
		self.port = port.strip()
		self.loop = loop.strip()

	def cek(self):		
		try:
			self.ser = Serial(self.port, 115200, timeout=5)
			return self.ser
		except:
			return 0

	def code(self):
		return self.start, self.stop

	def read(self):
		return self.ser.readline().decode()

	def write(self, data):
		return self.ser.write(str.encode(data))

	def setup(self):
		return self.loop

# if __name__ == "__main__":
# 	usb_port = usb_port()
	