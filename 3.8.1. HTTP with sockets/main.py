import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('IZZI-D362', '50A5DC5FD362')

wlan.status()
wlan.ifconfig()

import socket
ai = socket.getaddrinfo('google.com', 80)
addr = ai[0][-1]

s = socket.socket()
s.connect(addr)
s.send(b'GET/HTTP/1.0\r\n\r\n')

print(s.recv(512))