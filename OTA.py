import subprocess
OTA=subprocess.call(['sudo','git','pull'], shell=True)
print type(OTA)
print "OTA Updation success"
