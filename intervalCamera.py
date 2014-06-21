#!/usr/bin/python
 
import time
from config import *
from controlPort import *

print("press ^C to exit program ...\n")
 
ctrlPort = ControlPort() 
portTestInit()

try:
 while True:
     ctrlPort.sample()
     time.sleep(1)
     print "Yes\n" if ctrlPort.shouldWork() else "No\n"
except KeyboardInterrupt:
    print("detect key interrupt\n")
 
print("Program exit\n")

