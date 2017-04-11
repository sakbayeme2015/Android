install qpython and file qpython repertory in your android 

#!/usr/bin/env python

import subprocess
import os

def root_device():

 proc = subprocess.Popen('su' , stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

 command = ' cp /data/data/com.whatsapp/databases/wa.db /storage/emulated/0/' +\
           ' ; cp /data/data/com.whatsapp/databases/msgstore.db /storage/emulated/0/'

 (out,err) = proc.communicate(command)

 if proc.returncode !=0:
  os._exit(1)

root_device()
