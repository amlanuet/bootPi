# BootPi: Remote Control Boat
BootPi is a remote control boat powered by two DC motors, controlled via Electronic Speed Controllers (ESCs) and a Raspberry Pi. This guide will walk you through the steps to build your own BootPi.

## Table of Contents
Introduction
Components
Wiring Diagram
Software Setup
Running the Project
Troubleshooting
Acknowledgements
Introduction
BootPi is a DIY remote control boat project that uses a Raspberry Pi to control the speed and direction of two DC motors via ESCs. The boat is controlled remotely using a laptop connected to a WiFi network.

## Components
+ 1 x Raspberry Pi (any model with GPIO pins)
+ 2 x DC motors
+ 2 x ESC 120A
+ 4 x Batteries (2 for motors, 1 power bank for Raspberry Pi, 1 Makita + battery for network switch and WiFi bullet)
+ 1 x Network switch
+ 1 x WiFi bullet
+ 1 x Game controller
+ Various wires and connectors


## Wiring steps
1. Connect the DC motors to the ESCs.
2. Connect the ESCs signal wire to the Raspberry Pi GPIO pins (Pin 38 and Pin 40 for PWM signals). (on the ESC 120a this is a white wire)
3. Connect the batteries to their respective components:
4. Each motor negative to its own battery, And the positive to the manual switches and then to the battery.
5. Power bank to the Raspberry Pi.
6. Makita battery to the network switch and WiFi bullet.
7. Ensure all connections are secure and insulated.
8. UTP cable from bullet to switch, UTP cable from pi to switch 

## Software Setup
### Raspberry Pi
Install Raspbian OS on the Raspberry Pi.
Install necessary Python libraries:

```
sudo apt-get update
sudo apt-get install python3-pip
pip3 install pygame pigpio
sudo apt-get install python3-rpi.gpio
```

### Python Script on Raspberry Pi
Use bootServer2.py to listen for incoming TCP data and control the PWM signals. Run this script on your Raspberry Pi.

### Laptop
Install Python and necessary libraries.
Use joystickClientBoot.py to read the game controller input and send data to the Raspberry Pi. Run this script on your laptop that has the game controller plugged in.

## Running the Project
1. Power on all components.
2. Run the Python script on the Raspberry Pi.
3. Run the Python script on the laptop.
4. Use the game controller to control the boat.

## Troubleshooting
+ Ensure all connections are secure.
+ Verify the IP address of the Raspberry Pi.
+ Check the battery levels.
+ Ensure the Python scripts are running without errors.

## Acknowledgements
Special thanks to the Raspberry Pi community and all open-source projects I drew inspiration from.