# Write your code here :-)
from adafruit_circuitplayground.express import cpx

import board
import digitalio
import time

# LED_PIN = board.D13  # Pin number for the board's built in LED.
PIR_PIN = board.D2   # Pin number connected to PIR sensor output wire.

# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(PIR_PIN)
pir.direction = digitalio.Direction.INPUT

# Setup digital output for LED:
# led = digitalio.DigitalInOut(LED_PIN)
# led.direction = digitalio.Direction.OUTPUT

# Main loop that will run forever:

count = 0
scan = True
while True:
    # print(count)
    while scan:
        print("scanning")
        if pir.value:
            # PIR is detecting movement!
            if count < 5:
                count += 1
                # Count +1

            else:
                cpx.pixels[0] = (10, 0, 0)
                # cpx.play_tone(2000, 0.5)
                time.sleep(2.5)
                cpx.pixels[0] = (0, 0, 0)
                # print("ALARM!")
                count = 0
                # print("RESET")
                # Ongoing movement detected - Alarm! Count = 0.
            scan = False
            # print("flip")

        else:
            if count > 0:
                count -= 1
            else:
                count = 0
            scan = False

    else:
        scan = True
        # print("Restart")

    # print("sleep")
    time.sleep(2.5)