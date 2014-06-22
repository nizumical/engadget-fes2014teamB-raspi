import time
import picamera
from config import *

class MyCamera:
    def __init__(self):
        self.camera = picamera.PiCamera()
	self.camera.resolution = (1024, 768)
	self.camera.preview_fullscreen = False
	self.camera.preview_window = (200, 20, 512, 384)
	self.camera.start_preview()
        self.counter = 0
    def shot(self):
        filename = FOLDER + '/IMG%05d.JPG' % self.counter
	self.counter += 1
        self.camera.capture(filename)
        print(filename)
    def __del__(self):
	self.camera.stop_preview()
	self.camera.close()

