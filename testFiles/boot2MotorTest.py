import pygame
import pigpio
import time
import sys

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    print("Failed to connect to pigpio daemon")
    sys.exit(1)

# GPIO pins for ESC signals
ESC_LEFT_GPIO_PIN = 20
ESC_RIGHT_GPIO_PIN = 21

# Initialize pygame
pygame.init()
pygame.joystick.init()

# Function to set ESC speed
def set_speed(pin, speed):
    pi.set_servo_pulsewidth(pin, speed)

# Calibrate ESC
def calibrate_esc(pin):
    set_speed(pin, 2000)  # Maximum throttle
    time.sleep(2)
    set_speed(pin, 1000)  # Minimum throttle
    time.sleep(2)

# Arm ESC
def arm_esc(pin):
    set_speed(pin, 1500)
    time.sleep(1)

# Cleanup function to safely stop the ESCs
def cleanup():
    set_speed(ESC_LEFT_GPIO_PIN, 1500)  # Neutral throttle
    set_speed(ESC_RIGHT_GPIO_PIN, 1500)  # Neutral throttle
    time.sleep(1)
    pi.stop()
    pygame.quit()
    sys.exit()

# Calibrate and arm the ESCs
#calibrate_esc(ESC_LEFT_GPIO_PIN)
#calibrate_esc(ESC_RIGHT_GPIO_PIN)
#print("ESCs calibrated")
#arm_esc(ESC_LEFT_GPIO_PIN)
#arm_esc(ESC_RIGHT_GPIO_PIN)
#print("ESCs armed")

# Main loop to read controller input and adjust throttle
try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    while True:
        pygame.event.pump()

        # Left joystick vertical axis (axis 1) for left ESC
        left_axis_value = joystick.get_axis(1)
        print(f"Left Axis value: {left_axis_value}")

        # Implementing a dead zone for left joystick
        if abs(left_axis_value) < 0.1:
            left_axis_value = 0
            print("Left axis value within dead zone, set to 0")

        # Invert left axis value to correct forward/backward direction
        left_axis_value = -left_axis_value

        # Convert left axis value (-1 to 1) to throttle range (1000 to 2000)
        left_throttle = int((left_axis_value + 1) * 500 + 1000)

        # Set left ESC speed
        set_speed(ESC_LEFT_GPIO_PIN, left_throttle)
        print(f"Left Throttle: {left_throttle}")

        # Right joystick vertical axis (axis 3) for right ESC
        right_axis_value = joystick.get_axis(3)
        print(f"Right Axis value: {right_axis_value}")

        # Implementing a dead zone for right joystick
        if abs(right_axis_value) < 0.1:
            right_axis_value = 0
            print("Right axis value within dead zone, set to 0")

        # Invert right axis value to correct forward/backward direction
        right_axis_value = -right_axis_value

        # Convert right axis value (-1 to 1) to throttle range (1000 to 2000)
        right_throttle = int((right_axis_value + 1) * 500 + 1000)

        # Set right ESC speed
        set_speed(ESC_RIGHT_GPIO_PIN, right_throttle)
        print(f"Right Throttle: {right_throttle}")

        time.sleep(0.1)

except KeyboardInterrupt:
    cleanup()
except Exception as e:
    print(f"An error occurred: {e}")
    cleanup()
