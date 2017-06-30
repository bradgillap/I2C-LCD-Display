# Simple string program. Writes and updates strings.
# Gets the hostname and Ip address using built in python libraries.
# Demo program for the I2C 16x2 Display from Dealextreme
# Created by Bradley Gillap based on work from The Raspberry Pi Guy YouTube channel

# Import necessary libraries for commuunication and display use
import lcddriver    #Driver
import socket       #For host and IP
import time         #For general timers. Sleep etc.
import fcntl        #For host and IP
import struct
import json         #For pihole API
import urllib2      #For pihole API


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

display = lcddriver.lcd()                               #Load lcddriver and set it to display
ipaddy = get_ip_address('eth0')                         #Define Ip address variable
url = ("http://" + str(ipaddy) + "/admin/api.php")     #Connect to pihole API
data = json.load(urllib2.urlopen(url))                  #Populate data variable with API info

try:
    while True:
        data = json.load(urllib2.urlopen(url))                                  #Reload API Data In Loop
        blocked = data['ads_blocked_today']                                     #Assign API Data to variables
        percent = data['ads_percentage_today']
        queries = data['dns_queries_today']
        domains = data['domains_being_blocked']
        display.lcd_display_string("Host:" + str((socket.gethostname())), 1)    #Show host on screen max 16 chars
        display.lcd_display_string("IP:" + str(ipaddy), 2)                      #Show IP address on screen max 16 chars
        time.sleep(4)                                                           #Wait
        display.lcd_clear()                                                     #Clear the screen
        display.lcd_display_string("Blocked: " + str(blocked), 1)               #Show sites blocked on screen max 16 chars
        display.lcd_display_string("Percent: " + str(percent)+"%", 2)           #Show percentage of sites blocked max 16 chars
        time.sleep(4)
        display.lcd_clear()
        display.lcd_display_string("Queries: " + str(queries), 1)               #Show total queries on screen max 16 chars
        display.lcd_display_string("Domains: " + str(domains), 2)               #Show total domains in blocklist max 16 chars
        time.sleep(4)
        display.lcd_clear()
except KeyboardInterrupt:       # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()

