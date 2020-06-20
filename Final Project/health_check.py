#!/usr/bin/env python3

import psutil
import socket
import shutil

'''
This is the last part of the lab, where you will have to write a Python script named health_check.py that will run
in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution.
Moreover, this Python script should send an email if there are problems, such as:

    Report an error if CPU usage is over 80%
    Report an error if available disk space is lower than 20%
    Report an error if available memory is less than 500MB
    Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

Complete the script to check the system statistics every 60 seconds, 
and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:
'''

# variables for checking the
cpu = psutil.cpu_percent()
diskspace = psutil.disk_usage().percent
free_memory = psutil.swap_memory().free / 1000000
network = socket.gethostbyname('localhost')
subject_line = ""
email_body = "Please check your system and resolve the issue as soon as possible"

# checks if the cpu is in 80% usage
if cpu <= 80:
    print('CPU usage is over 80% usage, sending report now')
    subject_line = "Error - CPU usage is over 80%"

# checks if the disk space is over 80%
if diskspace <= 80:
    print('Disk space is over 80%, sending report')
    subject_line = "Error - Available disk space is less than 20%"

# checks if the available memory is less than 500MB
if free_memory < 500:
    print('Free memory is below 500MB, sending report')
    subject_line = "Error - Available memory is less than 500MB"

# checks if localhost resolves as 127.0.0.1
if network != '127.0.0.1':
    print('localhost does not resolve as 127.0.0.1, sending report')
    subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
