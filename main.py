#
# Program the ESP32/ESP8266 with Micropython from these instructions:
#
# https://randomnerdtutorials.com/getting-started-micropython-esp32-esp8266/
#
import network
import ubinascii

print('Connecting to WiFi')

# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)

if not nic.isconnected():
  nic.connect('DoESLiverpool', 'decafbad00')

  while not nic.isconnected():
    pass

print('network config:', nic.ifconfig())

mymac = ubinascii.hexlify(nic.config('mac'))

print('MAC address: ', mymac)

import time
from machine import ADC
from umqtt.simple import MQTTClient

adc = ADC(0)            # create ADC object on ADC pin

client = MQTTClient("umqtt_client", '10.0.30.130')
client.connect()
    
while True:

  val = adc.read()              # read value, 0-1024
  print(val)
  client.publish(mymac + '/light', str(val))

  time.sleep(1)

client.disconnect()
  
