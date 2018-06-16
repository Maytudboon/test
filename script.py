# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 09:36:11 2018

@author: Will Boon
"""

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = (socket.gethostname(), 8010)                                # change this to your ip address
sock.bind(server_address)
print (sys.stderr,'using %s port %s' % sock.getsockname())        # use this print statement for python3
sock.listen(1)

while True:
   print (sys.stderr, 'waiting for a connection')                 # use this print statement for python3
   connection, client_address = sock.accept()
   try:
       print (sys.stderr, 'client connected:', client_address)    # use this print statement for python3
       while True:
           data = connection.recv(1024)                           # change this value, based on your needs.
           print (sys.stderr, 'received "%s"' % data)             # use this print statement for python3
           if data:
               connection.sendall(data)
           else:
               break
   finally:
       connection.close()
