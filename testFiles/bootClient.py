import pygame
import socket
import time

# Initialize pygame
pygame.init()
pygame.joystick.init()

# Connect to the server
server_ip = '192.168.4.1'  # IP address of the Raspberry Pi
server_port = 65432
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Function to send joystick data to the server
def send_data(left_throttle, right_throttle):
    message = f"{left_throttle},{right_throttle}"
    client_socket.sendall(message.encode())

try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    while True:
        pygame.event.pump()

        # Left joystick vertical axis (axis 1) for left ESC
        left_axis_value = joystick.get_axis(1)
        if abs(left_axis_value) < 0.1:
            left_axis_value = 0
        left_axis_value = -left_axis_value
        left_throttle = int((left_axis_value + 1) * 500 + 1000)

        # Right joystick vertical axis (axis 3) for right ESC
        right_axis_value = joystick.get_axis(3)
        if abs(right_axis_value) < 0.1:
            right_axis_value = 0
        right_axis_value = -right_axis_value
        right_throttle = int((right_axis_value + 1) * 500 + 1000)

        # Send data to the server
        send_data(left_throttle, right_throttle)
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    client_socket.close()
    pygame.quit()
