# I2C-LCD-Display

Drivers and code for two very low cost LCD displays with instructions on how to setup each with python on a Raspberry Pi. This github repo has plenty of demo files I've collected from others or written myself to display some possibilities. 


![LCD running demo script.](https://github.com/bradgillap/I2C-LCD-Display/blob/master/example.jpg)

##Requirements
### Hardware
#### Screens

**16x2 LCD Screen**

http://www.dx.com/p/i2c-iic-lcd-1602-display-module-with-white-backlight-4-pin-cable-for-arduino-raspberry-pi-374741
##### OR
**20x4 LCD Screen**

http://www.dx.com/p/5v-iic-i2c-3-1-blue-screen-lcd-display-module-for-arduino-green-black-232993
#### Raspberry Pi 1/2/3
[https://www.raspberrypi.org/](https://www.raspberrypi.org/)
### Operating System
Any [raspbian](https://www.raspbian.org/) based operating system will work. I recommend [DietPi](http://dietpi.com/) for beginning your projects to reduce on overhead but novice users should use [raspbian](https://www.raspbian.org/).

##Connect LCD to Pi

***Step 1.*** Connect GND to GROUND. Pin 6

***Step 2.*** Connect VCC to 5V. Pin 2

***Step 3.*** Connect SDA to GPIO. Pin 3

***Step 4.*** Connect SCL to GPIO. Pin 5

Reference GPIO
![LCD running demo script.](https://github.com/bradgillap/I2C-LCD-Display/blob/master/gpioref2.png)


##Software Setup
We need to do a few things before you can begin running demo python scripts to display things on the LCD screen. Just follow the steps and you should be fine. If you are using the **root** account, you can ignore the **sudo** command. You only need to do these steps once.

We first need to enable the GPIO pins on the raspberrypi

***Step 1.*** Login to your pi through terminal or ssh and install the following packages.
```
sudo apt-get update -y && sudo apt-get install python-smbus git -y
```
***Step 2.*** Run this command to edit the modules file.
```
sudo nano /etc/modules
```
***Step 3.*** On the last line enter the following. If they already exist then just skip this step.
```
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
# Parameters can be specified after the module name.

snd-bcm2835     # This enables GPIO pins on the pi.
i2c-dev         # This enables i2c communication.
```
```
ctrl+o to save
```
***Step 4.*** Now we need to also turn on i2c everytime the pi boots.
```
sudo nano /boot/config.txt
```
***Step 5.*** Find the section for ***i2c*** and change the lines so they look like this. If you don't see these lines, go ahead and add them now.
```
#-------i2c-------------
dtparam=i2c_arm=on
dtparam=i2c1=on
i2c_arm_baudrate=100000
```
```
ctrl+o to save
```
***Step 6.*** clone this repository to your home directory.
```
cd ~
git clone https://github.com/bradgillap/I2C-LCD-Display
```

***Step 7.*** That's it! Now you can run any of the demo files. Just remember, each script requires lcddriver.py and i2c_lib.py to run. 

***Example 16x2 Display***
```
sudo python ~/I2C-LCD-Display/16x2LCD/demo_lcd.py
```
#### OR

***Run the script in the background***
```
sudo python ~/I2C-LCD-Display/16x2LCD/demo_lcd.py &
```

#### OR

***Run your script at boot every time***
```
sudo nano /etc/rc
#add this line to with a path to your script. Don't forget the and symbol
python /root/YOURLCDSCRIPT.py &
```
```
ctrl+o to save
```

