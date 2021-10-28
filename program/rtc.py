from datetime import datetime

class rtc:
	def time(self):
		waktu = str(datetime.now()).split(' ')
		waktu = ['']+waktu[0].split('-') + waktu[1].split(':')
		waktu[6] = waktu[6].split('.')[0]
		for x in range(len(waktu)):
			if x != 0:
				waktu[x] = str(int(waktu[x]))
		return '-'.join(waktu)

	def timeReverse(self):
		set_waktu = []
		waktu = self.time().split('-')
		count = 6
		for x in range(len(waktu)):
			if waktu[x] != '':
				set_waktu.append(waktu[count])
				count -= 1
		set_waktu.insert(3,'6')
		set_waktu = [''] + set_waktu
		return '-'.join(set_waktu)

	def day(self, kode):
		if kode == 0:
			days = {'sunday':'Minggu', 'monday':'Senin', 
					'tuesday':'Selasa', 'wednesday':'Rabu', 
					'thursday':'Kamis', 'friday':'Jumat', 'saturday':'Sabtu' }	
		else:
			days = {'sunday':'0', 'monday':'1', 
					'tuesday':'2', 'wednesday':'3', 
					'thursday':'4', 'friday':'5', 'saturday':'6' }		
		return days[datetime.today().strftime('%A').lower()]

# if __name__ == "__main__":
# 	rtc = rtc()
# 	print(rtc.time1())
