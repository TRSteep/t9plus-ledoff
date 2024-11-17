#!/usr/bin/env python3

# Turn Off LED light for T9Plus mini PC (N100 cpu)
# https://github.com/TRSteep/t9plus-ledoff
# Version 0.2
# "Off": 0x04 : 0
# "On": 0x02 : 254

import serial
import time

# SET LED status OFF
def send_led_status_off():
    """ Procedure to SET LED backlight OFF
    """
    try:
        # Open serial port
        s = serial.Serial('/dev/ttyUSB0', 10000) # LED controller
        # Send data with delays
        for i in (0xfa, 0x04, 1, 1, 0):
            s.write(bytes([i]))
            time.sleep(0.005)
        # Close serial port
        s.close()
        print("LED set OFF successfully")
    except Exception as e:
        print("An error occurred:", str(e))

# Turn OFF LED light
send_led_status_off()