import RPi.GPIO as GPIO
import time

#GPIO mode as bcm
GPIO.setmode(GPIO.BCM)

#assigning pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
LED = 16

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

pwm = GPIO.PWM(LED, 100)
pwm.start(0)

def distance():
    GPIO.output(GPIO_TRIGGER, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime-StartTime

    # sonic speed (34300 cm/s)
    distance = (TimeElapsed*34300)/2

    if(distance<=50):
        pwm.ChangeDutyCycle(100-distance*2)
        print('The object is = %.1f cm away' % distance)
        time.sleep(0.5)
    else:
        print('Nothing Close By')
        pwm.ChangeDutyCycle(0)
        time.sleep(1)

if __name__ == '__main__':
    try:
        while True:
            distance()

    except KeyboardInterrupt:
        print("Measurement stopped by User")

    finally:
       GPIO.cleanup()

# Tutorials by Raspberry Pi tutorials and Electronic Hobbyist was used and then
# changed to match requirements
