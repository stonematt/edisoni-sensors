#!/bin/bash
#script to load data into rrd archive on edison.
#script is called by crontab ever 5 minutes: */5 * * * * ~/rrd-bash.sh
python /home/root/edisoni-sensors/photocell-rrd-update.py
 
