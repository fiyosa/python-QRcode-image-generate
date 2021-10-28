from os import getcwd
from random import randint

class SN:
	def __init__(self, computer, digit, sn):
		self.computer = computer.strip()
		if int(digit) > 2:
			self.digit = int(digit.strip())-1
		else:
			self.digit = 2
		self.sn = sn

	def get(self):		
		s = open(getcwd()+'\\'+'database.db','r')
		self.database = s.read()
		if self.database == '':
			serial_number = '{:0{}d}'.format(randint(0, int('9'*self.digit)),self.digit)
		else:
			while 1:
				serial_number = '{:0{}d}'.format(randint(0, int('9'*self.digit)),self.digit)
				if self.database.find(self.computer+serial_number) == -1:
					break
		s.close()
		return self.sn+self.computer+serial_number

	def set(self,data):
		s = open(getcwd()+'\\'+'database.db','w')	
		s.write(self.database+'\n'+data)
		s.close()	

# if __name__ == "__main__":
# 	SN = SN('1','5', 'ISN')
# 	print(SN.get())
	# digit = '6'
	# serial_number = '{:0{}d}'.format(randint(0, int('9'*1)),1)
	# print('9'*0)


	