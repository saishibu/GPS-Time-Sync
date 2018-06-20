import subprocess
import datetime

try:
    subprocess.check_call("ntpdate") #Non-zero exit code means it was unable to get network time
except subprocess.CalledProcessError:
    dt = getRTCTime() # Get time from RTC as a datetime object
    subprocess.call(['sudo', 'date', '-s', '{:}'.format(dt.strftime('%Y/%m/%d %H:%M:%S'))], shell=True) #Sets system time (Requires root, obviously)

#Rest of code
