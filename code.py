# Write your code here :-)
# from adafruit_circuitplayground.express import cpx
from adafruit_circuitplayground.express import cpx
import board
import digitalio
import time
import pulseio
from adafruit_circuitplayground import cp
from adafruit_motor import servo

# LED_PIN = board.D13  # Pin number for the board's built in LED.
PIR_PIN = board.D2   # Pin number connected to PIR sensor output wire.

# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(PIR_PIN)
pir.direction = digitalio.Direction.INPUT

# create a PWMOut object on Pin A3.
pwm = pulseio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

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
                for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
                    my_servo.angle = angle
                    time.sleep(0.05)
                for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
                    my_servo.angle = angle
                    time.sleep(0.05)
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