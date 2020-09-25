import fcntl
import socket
import struct

#eth0 is the network port

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip=socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8915, # SIOCGIFADDR
    struct.pack('256s','eth0'[:15])
    )[20:24])
print(ip)



