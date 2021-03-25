#tudp_client.py
from socket import *

s = socket(type=SOCK_DGRAM)
s.sendto(b'Cao veliki pozdrav serveru od Ivan Pelivan',('localhost',5000))
data,addr = s.recvfrom(1024)
print(data,addr)