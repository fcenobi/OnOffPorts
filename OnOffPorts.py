import os
import telnetlib
import time
import subprocess

host = "192.168.1.1"
password = "password"
enable = "enable"
commands = ["configure terminal",
            "interface gigabitethernet 1/0/2",
            "interface gigabitethernet 1/0/3"]

onoff = ["shutdown",
         "no shutdown"]

tn = telnetlib.Telnet(host)
tn.set_debuglevel(1)
time.sleep(2)
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
time.sleep(2)
tn.write(enable.encode('ascii') + b"\n")
time.sleep(2)
tn.write(password.encode('ascii') + b"\n")
time.sleep(2)
tn.write(commands[0].encode('ascii') + b"\n")
time.sleep(2)
tn.write(commands[1].encode('ascii') + b"\n")
time.sleep(2)
tn.write(onoff[0].encode('ascii') + b"\n")
time.sleep(2)
tn.write(b"exit\n")
time.sleep(2)
tn.write(commands[2].encode('ascii') + b"\n")
time.sleep(2)
tn.write(onoff[0].encode('ascii') + b"\n")
time.sleep(2)
tn.write(b"exit\n")

time.sleep(5)
os.system("TASKKILL /F /IM Program.exe")
time.sleep(5)
subprocess.Popen(['C:\Programs\Program.exe'])
time.sleep(5)

tn.write(commands[1].encode('ascii') + b"\n")
time.sleep(2)
tn.write(onoff[1].encode('ascii') + b"\n")
time.sleep(2)
tn.write(b"exit\n")
time.sleep(2)
tn.write(commands[2].encode('ascii') + b"\n")
time.sleep(2)
tn.write(onoff[1].encode('ascii') + b"\n")
time.sleep(2)
tn.write(b"exit\n")
time.sleep(2)
tn.close()

