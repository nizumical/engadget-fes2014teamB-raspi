#!/bin/bash

sdpath=/media/FLASHAIR

# Wait for mounting SD card...
while [ ! -e $sdpath ]
do
  sleep 1s
done

# Start interval camera
sudo python intervalCamera.py
