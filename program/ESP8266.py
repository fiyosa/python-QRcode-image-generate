from time import sleep, time
from setup import setup
from rtc import rtc
from usbPort import usb_port
from serialNumber import SN
from sticker import sticker
from sys import exit

setup = setup()
if setup.check():
	system = setup.system()		
	try:
		sticker = sticker(system['pic_text'])
		rtc=rtc()
		SN = SN(system['computer'], system['digit'], system['sn'])
		usb_port = usb_port(system['start'], system['stop'], system['port'], system['loop'])
		start, stop = usb_port.code()

		reupload = 0
		reupload_stop = 0
		mulai = 0
		
		print('===================== Selamat Datang Computer {} ====================='.format(system['computer']))
		if system['test'] == "1":
			print('============================== TEST =================================')
		s = open('error.txt', 'w')
		s.write('')
		s.close()
	except Exception as e:
		s = open('error.txt', 'w')
		s.write('{}'.format(e))
		s.close()
		print('\n\nSYSTEM ERROR !!!\nSampai Jumpa :(')
		sleep(2)
		exit()

	while 1:
		try:
			while 1:
				if reupload == 0:
					check = input('Mulai proses? [y/n]: ')
					if check.upper() == 'Y' :
						mulai = 1
						print('Menghubungkan ke ESP8266 ...')
						if system['test'] == "1":  #------------ testing----------------
							mulai = 0
							reupload = 0
							if system['test_sn'] == '':
								serial_number = SN.get()
							else:
								SN.get()
								serial_number = system['test_sn']
							Test = ''#'-TEST'
							sticker.clear()
							sticker.generate(serial_number + Test)
							sticker.get(serial_number + Test)
							SN.set(serial_number + Test)							
							print(serial_number+' berhasil disimpan')
							print('\n')
							continue
						
					elif check.upper() == 'N':
						print('\nSampai Jumpa :)')
						sleep(2)
						break
					
				if mulai == 1 or reupload == 1:	
					mulai=0
					if reupload == 1:
						reupload = 0
						reupload_stop = 1
					ser = usb_port.cek() #--------------------------------------------------
					if ser != 0:
						if system['test_sn'] == '':
							serial_number = SN.get()
						else:
							SN.get()
							serial_number = system['test_sn']
						data_kirim = start+serial_number+rtc.time()+stop
						# print(data_kirim)
						usb_port.write(data_kirim) #--------------------------------------------------
						count = time()
						while 1:
							data_serial = usb_port.read() #--------------------------------------------------
							if data_serial.find(start) != -1 and data_serial.find(stop) != -1:
								data_serial = data_serial.split(start)[1].split(stop)[0] #--------------------------------------------------
								if data_serial == serial_number:
									print(data_serial+' berhasil disimpan')
									sticker.clear()
									sticker.generate(serial_number)
									sticker.get(serial_number)
									SN.set(serial_number)
									if usb_port.setup() == '1':
										ser.close() #
									break
								else:
									print('----------error----------')
									print('Terjadi kesalahan dalam upload Serial Number :(\n')
									break
							elif data_serial.find("???") != -1:
								print('----------error----------')
								print('Silahkan putuskan sambungan PORT lalu sambungkan kembali !!!\n')
								ser.close()
								break
							if time() - count >= 5.0:
								print('----------error----------')
								print('Terjadi kesalahan dalam upload Serial Number :(\n')
								break
					else:
						print('----------error----------')
						print('Silahkan sambungkan PORT ESP8266 !!!\n')
			break
					
		except KeyboardInterrupt:
			print('\n\nSampai Jumpa :)')
			sleep(2)
			break

		except:
			if reupload_stop == 0:
				reupload = 1
			else:
				reupload = 1
				reupload_stop = 0
			if system['test'] != "1": #------------ testing----------------
				ser.close() #--------------------------------------------------
			else:
				print('----------error----------')
				print('Internal Error test !!!')
else:
	print('----------error----------')
	print('\n\nSETUP ERROR !!!\nSampai Jumpa :(')
	sleep(2)
	

