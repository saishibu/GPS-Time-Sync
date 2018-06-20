import subprocess
OTA=subprocess.call(['sudo','git','pull'])
output,error= OTA.communicate()
print output
print error
