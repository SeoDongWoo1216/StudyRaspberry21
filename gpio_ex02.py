import RPi.GPIO as GPIO
import time

red = 19
yellow = 4
green = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

if __name__ == '__main__':
    while True:
        GPIO.output(red, False)
        GPIO.output(yellow, True)
        time.sleep(2)
        GPIO.output(yellow, False)
        GPIO.output(green, True)
        time.sleep(10)
        GPIO.output(green, False)
        GPIO.output(red, True)
        time.sleep(5)

