import pygame
import socket
import time

def main():
    # Initialize pygame
    pygame.init()
    pygame.joystick.init()

    # Setup client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.4.8', 65432))

    try:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        while True:
            pygame.event.pump()

            # Left joystick vertical axis (axis 1)
            left_axis_value = joystick.get_axis(1)
            if abs(left_axis_value) < 0.1:
                left_axis_value = 0
            left_axis_value = -left_axis_value
            left_throttle = int((left_axis_value + 1) * 500 + 1000)

            # Right joystick vertical axis (axis 3)
            right_axis_value = joystick.get_axis(3)
            if abs(right_axis_value) < 0.1:
                right_axis_value = 0
            right_axis_value = -right_axis_value
            right_throttle = int((right_axis_value + 1) * 500 + 1000)

            # Send data to server
            data = f"{left_throttle},{right_throttle}"
            client_socket.sendall(data.encode())

            time.sleep(0.1)

    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        pygame.quit()

while True:
    try:
        main()
    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting...")
        break
    except pygame.error as e:
        print(f"Joystick error: {e}")
    except socket.error as e:
        print(f"Socket error:{e}")
    except Exception as e:
        print(f"Restarting program due to error: {e}")
        time.sleep(1)  # Optional: wait a bit before restarting
