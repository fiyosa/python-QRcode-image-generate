pip install pyserial
pip install qrcode[pil]
pip instal pyinstaller => pyinstaller --clean --onefile --icon=logo.ico ESP8266.py usbPort.py setup.py serialNumber.py rtc.py sticker.py

database.db ===================================================
kumpulan data serial number yg disimpan secara local

start ===================================================
kode parse untuk esp8266 agar dapat saling mengirimkan data

stop ===================================================
kode parse untuk esp8266 agar dapat saling mengirimkan data

loop ===================================================
dapat melakukan upload serial number ke esp8266 secara berulang jika set "0" dan
cuma bisa upload sekali doang jika set "1"

digit ===================================================
jumlah digit pada serial number dengan ketentuan
ISN Computer {digit} = ISN 0 {123456}

port ===================================================
set serial COM? pada usb ESP8266

computer ===================================================
menandai local computer agar tidak sama saat generate serial port
