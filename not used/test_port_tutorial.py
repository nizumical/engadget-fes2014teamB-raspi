import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

if len(sys.argv) < 4:
    print "usage: myself port17 port21 port22"
    exit(0)

GPIO.output(17, int(sys.argv[1]))
GPIO.output(21, int(sys.argv[1]))
GPIO.output(22, int(sys.argv[1]))

#GPIO.cleanup()
