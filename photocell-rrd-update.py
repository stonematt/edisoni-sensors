#!/usr/bin/python

# env is a command that manages the environment.
# it's probably not setup on edison, so use the explicit path  
#!/usr/bin/env python  

#These are dependencies  
import mraa  
import time
from datetime import datetime
import sys
#This location of the python rrd.tool modules is included in the path:
sys.path.append('/usr/lib/python2.7/site-packages')
import rrdtool

#This command created our database
#ret = rrdtool.create("photocell.rrd", "--step","300", "--start", "now",
#                     "DS:photocell:GAUGE:100:U:U", "RRA:AVERAGE:0.5:1:600",
#                     "RRA:AVERAGE:0.5:6:100")

#Pin A0 on Edison receives photocell sensor data
pcell_pin=0
pcell_value=0
x=0
tally = 0
photocell = mraa.Aio(pcell_pin)
average = 0

while x < 10:

    #read photocell, add to tally, wait 1 second, repeat
    pcell_value=float(photocell.read())
    tally = tally + pcell_value
    time.sleep(.2)
    x = x + 1

average = tally/x
ret = rrdtool.update('/home/root/edisoni-sensors/photocell.rrd','N:%s' % average)
