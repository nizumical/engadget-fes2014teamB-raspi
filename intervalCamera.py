#!/usr/bin/python
 
import time
from config import *
from controlPort import *
from camera import *
from playBuzzer import *

class IntervalCounter:
    def __init__(self):
    	self.unmarkOneDone()
    def countUp(self):
        if self.isTimeToTakeNextPhoto(): return True  # not to increase too much
        self.count += 1
        return self.isTimeToTakeNextPhoto()
    def isTimeToTakeNextPhoto(self):
        return (INTERVAL <= self.count) or self.initial
    def isTheFirstTime(self):
	return self.initial
    def onOneShotDone(self):
        self.initial = False
        self.count = 0
    def unmarkOneDone(self):
        self.initial = True
        self.count = 0
    def __str__(self):
        return "(initial)" if self.initial else "" + "[" + str(self.count) + "]"

def stillNotTimeToShotNext(ctrlPort, intvlCount):
    return (not intvlCount.isTimeToTakeNextPhoto()) \
        or (not ctrlPort.shouldWork())

def logMeBaby(ctrlPort, intvlCount):
    print "distance:" + str(ctrlPort.distance()) \
        + " manual:" + str(ctrlPort.manual()) \
        + " intvlCnt:" + str(intvlCount)

def makeNoiseIfDisconnected(ctrlPort, intvlCount, playBuzzer):
    if 0 < ctrlPort.distance(): return
    if intvlCount.isTheFirstTime(): return
    playBuzzer.keepOnNoising()

##############################
print("press ^C to exit program ...\n")

camera = MyCamera()
playBuzzer = PlayBuzzer()
ctrlPort = ControlPort()
ctrlPort.sample()
portTestInit()

intvlCount = IntervalCounter()

try:
    while True:
        while stillNotTimeToShotNext(ctrlPort, intvlCount):
            makeNoiseIfDisconnected(ctrlPort, intvlCount, playBuzzer)
            logMeBaby(ctrlPort, intvlCount)
            ctrlPort.sample()  # takes 1 sec
            if not ctrlPort.shouldWork():
                intvlCount.unmarkOneDone()
            intvlCount.countUp()
        camera.shot()
        intvlCount.onOneShotDone()
except KeyboardInterrupt:
    print("detect key interrupt\n")
 
print("Program exit\n")

