import time
import network
import urequests as requests

ssid = 'IZZI-D362'
pw = '50A5DC5FD362'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, pw)

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
    
while True:
    headers = ...
    payload = ...
    
    try:
        print('Sending...')
        response = requests.post('A remote end point', headers = headers, data = payload)
        print('Sent(' + str(response.status_code) + "), status = " + str(wlan.status()))
        response.close()
    except:
        print('Could not connect (status = ' + str(wlan.status()) + ")")
        if wlan.status() < 0 or wlan.status() >= 3:
            print('Trying to reconnect...')
            wlan.disconnect()
            wlan.connect(ssid, pw)
            if wlan.status() == 3:
                print('Connected')
            else:
                print('Failed')
    time.sleep(5)