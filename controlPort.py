import time
import RPi.GPIO as GPIO
from myMathUtil import *
from config import *

def readPort(portNo):
    return GPIO.input(portNo)

class ControlPort:
    def __init__(self):
        self.bmaDist0 = BinaryMovingAeverage(portDistance0, L)
        self.bmaDist1 = BinaryMovingAeverage(portDistance1, L)
        self.bmaMan   = BinaryMovingAeverage(portManual,    L)
        self.haveConnected = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(portDistance0, GPIO.IN)
        GPIO.setup(portDistance1, GPIO.IN)
        GPIO.setup(portManual, GPIO.IN)
    def __del__(self):
        GPIO.cleanup()
        pass
    def sample(self):
        # takes 1 sec for sampling
        for i in range(numOfSample):
            self.bmaDist0.update(readPort(portDistance0))
            self.bmaDist1.update(readPort(portDistance1))
            self.bmaMan.update(readPort(portManual))
            time.sleep(1.0 / numOfSample)
        if 0 < self.distance():
            self.haveConnected = True
    def distance(self):
        dist = (self.bmaDist1.evaluate() << 1) + self.bmaDist0.evaluate()
        return dist
    def manual(self):
        return self.bmaMan.evaluate()
    def shouldWork(self):
        """evaluate if it's time to take photos or not"""
        if not self.haveConnected: return False
        if self.distance() <= distanceThreshold: return True
        if self.manual() == H: return True
        return False

