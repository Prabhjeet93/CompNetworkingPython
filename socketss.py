"""
        Sockets-:
            Sockets are what we can used to connect two nodes together.
            we're going use this to connect ports to ip addresses.
            if port is open we will make connection.

            http - 80
            https - 443
            ftp - 21

            netcat - nc
                it allows us to connect to connect to open ports or estabilish listener on an open port
                $ nc -nvlp 7777

"""

import socket

HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af_inet is ipv4, sock_stream is port
s.connect((HOST, PORT))

