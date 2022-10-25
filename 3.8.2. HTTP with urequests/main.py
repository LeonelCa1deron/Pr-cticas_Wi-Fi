import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('IZZI-D362', '50A5DC5FD362')

import urequests
r = urequests.get('http://www.google.com')
print(r.content)
r.close()