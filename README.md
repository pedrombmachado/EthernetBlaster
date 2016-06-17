# EthernetBlaster
Ethernet Blaster

### Application ###

* Ehernet Blaster: 1.3
* Recommended OS: Ubuntu 16.04 LTS 64 bits
* Python 3.5

### Hardware requirements ###
The following parts are required:
1)Minnowboard Turbot;
2)Micro-HDMI to HDMI cable;
3)PSU 5V@2A;
4)USB stick for installing the Ubuntu Server;
6)Monitor

### Set up the Minnowboard Turbot ###
* Download Ubuntu server 16.04 LTS AMD64 from www.ubuntu.com
* Prepare a booting USB stick using UnetBootIn
* Install the Ubuntu server on the Minnowboard Turbot

### Install and configure the quartus programmer ###
* Download and install the QuartusProgrammerSetup-16.0.0.211-linux.run from Altera website
* Install the QuartusProgrammerSetup-16.0.0.211-linux.run by running the following commands:
$ sudo chmod -R QuartusProgrammerSetup-16.0.0.211-linux.run
$ sudo ./QuartusProgrammerSetup-16.0.0.211-linux.run

* Configure the Usb-blaster driver
$ sudo nano /etc/udev/rules.d/92-usbblaster.rules

* Add the following data to the file:
# USB-Blaster
SUBSYSTEM=="usb", ATTRS{idVendor}=="09fb", ATTRS{idProduct}=="6001", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="09fb", ATTRS{idProduct}=="6002", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="09fb", ATTRS{idProduct}=="6003", MODE="0666"
# USB-Blaster II
SUBSYSTEM=="usb", ATTRS{idVendor}=="09fb", ATTRS{idProduct}=="6010", MODE="0666"
SUBSYSTEM=="usb", ATTRS{idVendor}=="09fb", ATTRS{idProduct}=="6810", MODE="0666"

* Reload udev rules
$ sudo udevadm control --reload-rules


### Set up the ethernetBlaster.py as a service ##
$ sudo apt-get install upstart upstart-sysv python3-pip python3-requests python3-urllib3

# Set up the environment and preparing the python script:
$ mkdir ~/Ethernet_Blaster
$ cd ~/Ethernet_Blaster
$ mkdir received
* Place the ethernetBlaster.py inside of the folder Ethernet_Blaster

* Edit the ethernetBlaster.py script and adapt the path name and ip address
* Test the script by running the following command on the Minnoboard Turbot:
$ python3 ethernetBlaster.py

* Edit the sendSof.py script and adapt the path name and ip address
* And run the following command on the client computer:
$ python3 sendSof.py <file name>

* NOTE that at this stage you may have to install some python libraries.
* The next step is to create a service to automatically load the script as a service.
* edit the file ethernetBlaster.conf and correct the folder location and copy it to the /etc/init/
* Reboot the Minnoboard Turbot and test it

### Contacts ###

* Pedro Machado <pedro.baptistamachado@ntu.ac.uk>
* Alicia Costalago Meruelo <alicia.costalagomeruelo@ntu.ac.uk>
* Kofi Appiah <kofi.appiah@ntu.ac.uk>
* Martin McGinnity <martin.mcginnity@ntu.ac.uk>
