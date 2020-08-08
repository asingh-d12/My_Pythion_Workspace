import subprocess
import time

while True:
    op = subprocess.getoutput('ping -c 1 google.com')
    if not "Temporary failure in name resolution" in op:
        subprocess.call('killall clementine'.split())
        break
    else:
        print("Internet still down!!")
        time.sleep(300)
