import socket
import pigpio
import sys

# Initialize pigpio
pi = pigpio.pi()
if not pi.connected:
    print("Failed to connect to pigpio daemon")
    sys.exit(1)

# GPIO pins for ESC signals
ESC_LEFT_GPIO_PIN = 20
ESC_RIGHT_GPIO_PIN = 21

# Function to set ESC speed
def set_speed(pin, speed):
    pi.set_servo_pulsewidth(pin, speed)

# Setup server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 65432))
server_socket.listen(1)
print("Server listening on port 65432")

try:
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        left_throttle, right_throttle = map(int, data.split(','))
        set_speed(ESC_LEFT_GPIO_PIN, left_throttle)
        set_speed(ESC_RIGHT_GPIO_PIN, right_throttle)
        print(f"Left Throttle: {left_throttle}, Right Throttle: {right_throttle}")

except KeyboardInterrupt:
    pass
finally:
    conn.close()
    server_socket.close()
    pi.stop()