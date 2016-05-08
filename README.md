# I2C-LCD-Display

Drivers and code for two very low cost LCD displays with instructions on how to setup each with python on a Raspberry Pi. This github repo has plenty of demo files I've collected from others or written myself to display some possibilities. 

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

##Software Setup
We need to do a few things before you can begin running demo python scripts to display things on the LCD screen. Just follow the steps and you should be fine. If you are using the **root** account, you can ignore the **sudo** command.

We first need to enable the GPIO pins on the raspberrypi

***Step 1.*** Login to your pi through terminal or ssh.

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
