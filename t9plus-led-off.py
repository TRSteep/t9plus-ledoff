#!/usr/bin/env python3

# Turn Off LED light for T9Plus mini PC
# Version 0.1
# "Off": 0x04 : 0
# "On": 0x02 : 254

import serial
import time

# SET LED status
def send_led_status(serial_port, baud_rate, mode, brightness, speed):
    try:
        # Open serial port
        s = serial.Serial(serial_port, baud_rate)
        # Send data with delays
        for b in (0xfa, mode, brightness, speed, 0):
            s.write(bytes([b]))
            time.sleep(0.005)
 
        # Close serial port
        s.close()
        print("LED status sent successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

send_led_status('/dev/ttyUSB0', 10000, 0x04, 1, 1)