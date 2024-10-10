import pygame
import pigpio
import time
import sys

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    print("Failed to connect to pigpio daemon")
    sys.exit(1)

# GPIO pin for ESC signal
ESC_GPIO_PIN = 20

# Initialize pygame
pygame.init()
pygame.joystick.init()

# Function to set ESC speed
def set_speed(speed):
    pi.set_servo_pulsewidth(ESC_GPIO_PIN, speed)

# Calibrate ESC
def calibrate_esc():
    set_speed(2000)  # Maximum throttle
    time.sleep(2)
    set_speed(1000)  # Minimum throttle
    time.sleep(2)
    #set_speed(1500)  # Neutral throttle
    #time.sleep(1)

# Arm ESC
def arm_esc():
    set_speed(1500)
    time.sleep(1)

# Cleanup function to safely stop the ESC
def cleanup():
    set_speed(1500)  # Minimum throttle
    time.sleep(1)
    pi.stop()
    pygame.quit()
    sys.exit()

# Calibrate and arm the ESC
#calibrate_esc()
#print("ESC calibrated")
#arm_esc()
#print("ESC armed")

# Main loop to read controller input and adjust throttle
try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    while True:
        pygame.event.pump()

        # Assuming the throttle is controlled by the left stick's vertical axis (axis 1)
        axis_value = joystick.get_axis(1)
        print(f"Axis value: {axis_value}")

        # Implementing a dead zone
        if abs(axis_value) < 0.1:
            axis_value = 0
            print("Axis value within dead zone, set to 0")

        # Invert axis value to correct forward/backward direction
        axis_value = -axis_value

        # Convert axis value (-1 to 1) to throttle range (1000 to 2000)
        throttle = int((axis_value + 1) * 500 + 1000)

        # Set ESC speed
        set_speed(throttle)
        print(f"Throttle: {throttle}")

        time.sleep(0.1)

except KeyboardInterrupt:
    cleanup()
except Exception as e:
    print(f"An error occurred: {e}")
    cleanup()
