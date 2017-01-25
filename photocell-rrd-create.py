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

# ret = rrdtool.create("photocell.rrd", "--step","300", "--start", "0","DS:photocell:GAUGE:330:U:U", "RRA:AVERAGE:0.5:1:600","RRA:AVERAGE:0.5:6:100")

# create a db with longer history and increasing aggregations
ret = rrdtool.create(
  "photocell.rrd", "--step","300", "--start", "0",
  "DS:photocell:GAUGE:330:U:U", 
  # "RRA:AVERAGE:0.5:1:600", -- commented by stone
  # "RRA:AVERAGE:0.5:6:100" -- commented by stone
  "RRA:AVERAGE:0.5:1:576"   #keep 5m values for 2d
  "RRA:AVERAGE:0.5:3:960"   #keep 15m values for 10d
  "RRA:AVERAGE:0.5:12:1080"   #keep 1h values for 45d
  "RRA:AVERAGE:0.5:48:4368"   #keep 4h values for 104w
  "RRA:MAX:0.5:1:576"   #keep 5m values for 2d
  "RRA:MAX:0.5:3:960"   #keep 15m values for 10d
  "RRA:MAX:0.5:12:1080"   #keep 1h values for 45d
  "RRA:MAX:0.5:48:4368"   #keep 4h values for 104w
  "RRA:MIN:0.5:1:576"   #keep 5m values for 2d
  "RRA:MIN:0.5:3:960"   #keep 15m values for 10d
  "RRA:MIN:0.5:12:1080"   #keep 1h values for 45d
  "RRA:MIN:0.5:48:4368"   #keep 4h values for 104w
)


# check out this RRA calculator I created: https://goo.gl/wg76Ef.

#"step" is the interval in seconds between each database entry
#"DS:photocell.GAUGE:330:U:U" Data Source is GAUGE, '330 is the timeout value in seconds - if no data is added, null entry will be archived
# "U:U" specifies unlimited min and max values
#  RRA:CF:xff:steps:rows
# "RRA:AVERAGE:0.5:1:600"  averages 1 value every 5 minutes -so there no average, just one reading reading). 600 database entries (600 x 5 min = 50 hours)
# "RRA:AVERAGE:0.5:6:100"  averages 6 values, writes an entry every 6 x 5 minutes = 30 minutes. 100 database entries (100 x 30 min = 50 hours) 

# 
#from http://apfelboymchen.net/gnu/rrd/create/
# rrdtool create download.rrd \
#         --step 300 \
#         DS:inet_down_total:DERIVE:600:0:U \
#         RRA:AVERAGE:0.5:1:288 \
#         RRA:AVERAGE:0.5:3:672 \
#         RRA:AVERAGE:0.5:12:744 \
#         RRA:AVERAGE:0.5:72:1460
#
# creates a database that
# * is updated every 5 minutes
# * has for data sources that that can save values from 0 to unlimited
# * saves 1 day in 5-minute resolution (288 * (300*1/60) / 60/24)
# * saves 1 week in in 15-minute resolution (672 * (300*3/60) / 60/24) 
# * saves 1 month in 1-hour resolution (744 * (300*12/60) / 60/24)
# * saves 1 year in 6-hour resolution (1460 * (300*72/60) / 60/24)

# personally I like overlap of the time cycle (you did the same w/ your inital aggregation keeping 50hr), 
# so I could always see "this period last time" in otherwords if today is Monday, and I'm looking at weekly data, 
# I like to look at last Sunday and Monday (not starting at Tuesday)
