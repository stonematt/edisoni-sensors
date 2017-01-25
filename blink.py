#!/usr/bin/python

# env is a command that manages the environment.
# it's probably not setup on edison, so use the explicit path  
#!/usr/bin/env python  

#These are dependencies  
import mraa  
import time

#13 is built in led
led = mraa.Gpio(13)  
led.dir(mraa.DIR_OUT)  
  
while True:  
    led.write(1)  
    time.sleep(0.2)  
    led.write(0)  
    time.sleep(0.8)
