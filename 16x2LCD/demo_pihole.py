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

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

#Get the hostname
socket.gethostbyname(socket.gethostname())

#Get the IP address
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

#Define ipaddy variable
ipaddy = get_ip_address('eth0')

#Connect to API and retrieve everything into the data variable
url = ("http://" + str(ipaddy) + "/pihole/api.php")   #CHANGE TO YOUR PIHOLE ADDRESS

try:
    while True:
        data = json.load(urllib2.urlopen(url))
        # Assign each api entry to a variable
        blocked = data['ads_blocked_today']
        percent = data['ads_percentage_today']
        queries = data['dns_queries_today']
        domains = data['domains_being_blocked']
        # Remember that your sentences can only be 16 characters long!
        display.lcd_display_string("Host:" + str((socket.gethostname())), 1)
        display.lcd_display_string("IP:" + str(ipaddy), 2)
        time.sleep(4)
        display.lcd_clear()
        display.lcd_display_string("Blocked" + str(blocked), 1)
        display.lcd_display_string("Percent:" + str(percent)+"%", 2)
        time.sleep(4)
        display.lcd_clear()
        display.lcd_display_string("Queries: " + str(queries), 1)
        display.lcd_display_string("Domains: " + str(domains), 2)
        time.sleep(4)
        display.lcd_clear()
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
