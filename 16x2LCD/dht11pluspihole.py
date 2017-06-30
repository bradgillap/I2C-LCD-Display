# A combination of both the DHT and pihole scripts
# Requires adafruit python DHT11, DHT22 Library. See other DHT script
# Bradley Gillap 2016

import lcddriver			#Driver
import socket				#For host and IP
import time					#For general timers. Sleep etc.
import fcntl				#For host and IP
import struct
import json					#For pihole API
import urllib2				#For pihole API
import Adafruit_DHT as dht	#Arguments dht instead of Adafruit_DHT, DHT11 device, GPIO26

#Initialize IP Address Check
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

#Initialize Hostname Check
socket.gethostbyname(socket.gethostname())

#VARIABLES
# If you use something from the driver library use the "display." prefix first
pin = 26												#GPIO pin we are communicating on CHANGE THIS
h,t = dht.read_retry(dht.DHT11, pin)					#Refreshes the DHT sensor. ARG DHT11 or DHT22 sensor
temp =  'Temp : {0:0.1f}C'.format(t)						#Store temp string info 
humid = 'Humid: {1:0.1f}%'.format(t,h)				#Store Humidity info
display = lcddriver.lcd()                               #Load lcddriver and set it to display
ipaddy = get_ip_address('eth0')                         #Define Ip address variable
url = ("http://" + str(ipaddy) + "/admin/api.php")     #Connect to pihole API

#INIT FUNCTIONS KILLING KITTENS
def pihole_hit():								#Function to poll the API for pihole.					
	global data
	global blocked
	global percent
	global queries
	global domains
	data = json.load(urllib2.urlopen(url))		#Store pihole api data.
	blocked = data['ads_blocked_today']
	percent = data['ads_percentage_today']
	queries = data['dns_queries_today']
	domains = data['domains_being_blocked']

def temp_hit():									#Poll the temp sensor and update vars
	global h,t
	global temp
	global humid
	h,t = dht.read_retry(dht.DHT11, pin)		#Change sensor here DHT11, DHT22 etc
	temp =  'Temp : {0:0.1f}C'.format(t)			#Formatting
	humid = 'Humid: {1:0.1f}%'.format(t,h)	#Formatting don't really understand these args

#DISPLAY FUNCTIONS to output to the lcd.
def net_info():
    display.lcd_clear()
    display.lcd_display_string("Host:" + str((socket.gethostname())), 1)    #Show host 
    display.lcd_display_string("IP:" + str(ipaddy), 2)                      #Show IP address 

def pi_info1():
    display.lcd_clear()
    display.lcd_display_string("Blocked: " + str(blocked), 1)               #Show sites blocked on screen max 16 chars
    display.lcd_display_string("Percent: " + str(percent)+"%", 2)           #Show percentage of sites blocked max 16 chars

def pi_info2():
    display.lcd_clear()
    display.lcd_display_string("Queries: " + str(queries), 1)       		#Show total queries on screen max 16 chars
    display.lcd_display_string("Domains: " + str(domains), 2)               #Show total domains in blocklist max 16 chars

def temp_info():
	display.lcd_clear()
	display.lcd_display_string(temp, 1)										#write temp to screen
	display.lcd_display_string(humid, 2)									#write humdity to screen


#Infinite Loop to Screen
lcdloop = 1
while lcdloop == 1 :  # This constructs an infinite loop
	pihole_hit()
	temp_hit()
	net_info()
	time.sleep(4)
	pi_info2()
	time.sleep(4)
	pi_info1()
	time.sleep(4)
	temp_info()
	time.sleep(4)
