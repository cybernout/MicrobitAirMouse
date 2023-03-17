import serial
import time
import subprocess


"""
Leslie 101Labs 2023

depends on : xdotool | pip3 install pyserial | and adduser permissions dialout

nice example to work with 

https://openprocessing.org/sketch/767863

to launch use chromium-browser --kiosk

crtl+t to get terminal and quit ;)

the micropython code to flash to the microbit 

SCALE_FACTOR = 100

while True:
    # Get the accelerometer data
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    
    # Scale down the data
    x = x // SCALE_FACTOR
    y = y // SCALE_FACTOR
    
    # Send the data over serial
    print("{},{}".format(x, y))

    # Delay for a short time
    sleep(20)

"""

ser = serial.Serial('/dev/ttyACM0', 115200)

try:
    while True:
        try:
            line = ser.readline().decode().strip()
            x, y = map(int, line.split(','))
        except ValueError:
            continue

        print(f"x: {x}, y: {y}")

        # Send mouse move event
        if x >= 0 and y >= 0:
            subprocess.run(['xdotool', 'mousemove_relative', str(x), str(y)])
        else:
            subprocess.run(['xdotool', 'mousemove_relative', '--', str(x), str(y)])

        # Delay for a short time to slow down data transmission
        time.sleep(0.01)
except KeyboardInterrupt:
    print("   your out --> Exiting...")
finally:
    ser.close()

