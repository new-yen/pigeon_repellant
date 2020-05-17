# Write your code here :-)
import board
import digitalio
import time
import pulseio
from adafruit_circuitplayground.express import cpx
from adafruit_motor import servo                    # from adafruit_circuitplayground import cp

# Setup digital input for PIR sensor:
PIR_PIN = board.D2                                  # Pin number connected to PIR sensor output wire.
pir = digitalio.DigitalInOut(PIR_PIN)
pir.direction = digitalio.Direction.INPUT

# create a PWMOut object on Pin A3.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

my_servo.angle = None
count = 0
scan = True

# Main loop that will run forever:
while True:
    while scan:
        print("scanning")
        if pir.value:                               # PIR is detecting movement!
            if count < 25:
                count += 1                          # Count +1

            else:
                print("ALARM!")                     # Movement detected - Alarm! Light, Sound, Motion, Count = 0
                
                cpx.pixels[0] = (10, 0, 0)
                # cpx.play_file("bird_caw1.wav")
                time.sleep(1)
                cpx.pixels[0] = (0, 0, 0)

                for angle in range(0, 180, 10):     # 0 - 180 degrees, 15 degrees at a time.
                    my_servo.angle = angle
                    time.sleep(0.01)

                time.sleep(5)
                my_servo.angle = None

                for angle in range(180, 0, -10):    # 180 - 0 degrees, 15 degrees at a time.
                    my_servo.angle = angle
                    time.sleep(0.01)

                my_servo.angle = None
                count = 0                  

            scan = False

        else:
            if count > 0:
                count -= 1
            else:
                count = 0
            scan = False

    else:
        scan = True

    print(count)
    time.sleep(0.25)