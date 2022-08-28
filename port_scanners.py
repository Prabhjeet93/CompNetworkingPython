import sys
import socket
from datetime import datetime

# Define  our target
if len(sys.argv) == 2:
    target = socket.gethostname(sys.argv[1])  # Translate hostname to IPV4
else:
    print(" Invalid number of arguments")
    print(" syntax is python3 scanner.py <ip address>")


# Adding banner
print("#"*60)
print("@"*50)
print("Scanning the target : ",target)
print("Time started : ",str(datetime.now()))

try:
    for port in range(50,90):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # af_inet is ipv4, sock_stream is port
        socket.setdefaulttimeout(2)   # setting the time to check the connection of port with ip address
        result = s.connect_ex((target,port))  # if port is open it means coonection is there, so it will return, if port is closed then it will 1
        if result == 0:
            print(f"Port {port} is open")
        else:
            pass
        s.close()
except KeyboardInterrupt:
    print("\n Exiting the Scanner Program")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to the server.")
    sys.exit()

print("@"*50)
print("#"*60)


# Output
# ############################################################
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Scanning the target :  11.11.11.11
# Time started :  2022-08-27 22:57:00.839143
# Port 53 is open
# Port 80 is open
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ############################################################
