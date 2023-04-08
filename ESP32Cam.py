import machine
from machine import Pin
import time
import camera

flash = Pin(4, Pin.OUT)   #set GPIO-4 Pin as output
flash.value(1)            #set the GPIO-4 Pin High
time.sleep(1)             #delay of 1 second
flash.value(0)            #set the GPIO-4 Pin Low

uos.mount(machine.SDCard(), "/sd")  #mount sd card

camera.init(1)                      #Initialize the camera 
camera.quality(12)
camera.framesize(9)                 #set the frame size as 1024*768

count = 0                             #create a counter variable and store 0

while True:                           #create an infinite loop
    if count == 2200:                 #if the value inside the counter variable reaches 2200
        flash.value(1)                #set the GPIO-4 Pin High
        print("Captured all the images")  #Print the string
        break
    buf = camera.capture()            #store the captured picture in the buffer
    file = open('/sd/images/'+str(count)+'.jpg','wb')  #create a new jpg file
    file.write(buf)                                  #store the buffer value inside the file
    file.close()                                     #close the file
    print(str(count)+'.jpg is captured')             #print the string
    
    count += 1               #increse the value of counter by one
    time.sleep(1)            #create a delay of 1 second
print("Work done!")  #print the string
