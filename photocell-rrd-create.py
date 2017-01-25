#!/usr/bin/python

# env is a command that manages the environment.
# it's probably not setup on edison, so use the explicit path  
#!/usr/bin/env python  

#These are dependencies  
import mraa  
import time
import sys
#This location of the python rrd.tool modules is included in the path:
sys.path.append('/usr/lib/python2.7/site-packages')
import rrdtool

ret = rrdtool.create("photocell.rrd", "--step","300", "--start", "0","DS:photocell:GAUGE:330:U:U", "RRA:AVERAGE:0.5:1:600","RRA:AVERAGE:0.5:6:100")

#"step" is the interval in seconds between each database entry
#"DS:photocell.GAUGE:330:U:U" Data Source is GAUGE, '330 is the timeout value in seconds - if no data is added, null entry will be archived
# "U:U" specifies unlimited min and max values
# "RRA:AVERAGE:0.5:1:600"  averages 1 value every 5 minutes -so there no average, just one reading reading). 600 database entries (600 x 5 min = 50 hours)
# "RRA:AVERAGE:0.5:6:100"  averages 6 values, writes an entry every 6 x 5 minutes = 30 minutes. 100 database entries (100 x 30 min = 50 hours) 
