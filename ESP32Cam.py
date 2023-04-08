import machine
from machine import Pin
import time
import camera

flash = Pin(4, Pin.OUT)
flash.value(1)
time.sleep(1)
flash.value(0)

uos.mount(machine.SDCard(), "/sd")  #mount sd card

camera.init(1)
camera.quality(12)
camera.framesize(9) #1024x768

count = 0

while True:
    if count == 2200:
        flash.value(1)
        print("captured the images")
        break
    buf = camera.capture()
    file = open('/sd/pics/'+str(count)+'.jpg','wb')
    file.write(buf)
    file.close()
    print(str(count)+'.jpg is captured')
    
    count += 1
    time.sleep(1)
print("Done all  the work")
