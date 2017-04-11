#install qpython in your android device

#!/usr/bin/env python

import subprocess

def root_device():

 proc = subprocess.Popen('su')
 (out,err) = proc.communicate('ping -c 5 127.0.0.1') #communicate with ping  command

root_device()
