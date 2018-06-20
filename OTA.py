import subprocess
OTA=subprocess.call(['sudo','git','pull'])
print type(OTA)
