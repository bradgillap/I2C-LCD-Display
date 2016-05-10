# Temperature / humdiity detector using a DHT11 or DHT22 sensor
# REQUIRES ADAFRUIT LIBRARY INSTALLED

# INSTRUCTIONS: git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# INSTRUCTIONS: sudo apt-get install build-essential python-dev python-openssl
# INSTRUCTIONS: sudo python setup.py install
# INSTRUCTIONS: FIND DHT11 or DHT22 INFO ONLINE FOR CONNECTING. 10k resister required
#Written by Bradley Gillap 2016

import Adafruit_DHT as dht	#Arguments dht instead of Adafruit_DHT, DHT11 device, GPIO26
import lcddriver
import time

#Assign to variables

pin = 26   					#GPIO pin we are communicating on CHANGE THIS
h,t = dht.read_retry(dht.DHT11, pin)		#Refreshes the DHT sensor. ARG DHT11 or DHT22 sensor
display = lcddriver.lcd()			#Refering to the LCD
temp = 'Temp:{0:0.1f} C'.format(t)		#Store temp string info 
humid = 'Humidity:{1:0.1f}%'.format(t,h)	#Store Humidity info

try:
	while True:
			h,t = dht.read_retry(dht.DHT11, pin)		#Loop the check sensor check DHT11 or DHT22 sensor 
			temp = 'Temp:{0:0.1f} C'.format(t)		#Update variable temperature
			humid = 'Humidity:{1:0.1f}%'.format(t,h)	#Update variable humidity
			display.lcd_clear()				#Clear screen
			display.lcd_display_string(temp, 1)		#write temp to screen
			display.lcd_display_string(humid, 2)		#write humdity to screen
			time.sleep(2)
 
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
