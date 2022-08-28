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
                $ nc -nvlp 7770

        How to Run this script.
            step1. open terminal in Kali linux and run below command
                    $ nc -nvlp <port>   -> $ nc -nvlp 7770
            step2. Open another terminal in Kali linux and execute this python script or below code.

            After that "$ nc -nvlp 7777" this commands output will show that connection estabilish
"""

import socket

HOST = '127.0.0.1'
PORT = 7770

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af_inet is ipv4, sock_stream is port
s.connect((HOST, PORT))

