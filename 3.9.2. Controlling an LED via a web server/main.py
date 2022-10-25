import network
import socket
import time

from machine import Pin

led = Pin(15, Pin.OUT)

ssid = 'IZZI-D362'
pw = '50A5DC5FD362'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, pw)

html = """<!DOCTYPE html>
<html>
    <head> <title>Pico W</title> </head>
    <body> <h1>Pico W</h1>
        <p>%s</p>
    </body>
</html>
"""

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
    time.sleep(1)
    
if wlan.status() != 3:
    raise RuntimeError('Network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print('IP = ' + status[0])

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)

while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        print(request)
        
        request = str(request)
        led_on = request.find('/light/on')
        led_off = request.find('/light/off')
        print('led on = ' + str(led_on))
        print('led off = ' + str(led_off))
        
        if led_on == 6:
            print('led_on')
            led.value(1)
            stateis = 'LED is ON'
            
        if led_off == 6:
            print('led_off')
            led.value(0)
            stateis = 'LED is OFF'
            
        response = html % stateis
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    
    except OSError as e:
        cl.close()
        print('Connection closed')