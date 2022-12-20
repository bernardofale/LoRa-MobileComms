from network import LoRa
import socket
import time
from machine import Pin
import machine



# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

i = 0
if i == 0:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(12)
#bit rate = 440 bit/s
elif i == 1:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(11)
#bit rate = 980 bit/s
elif i == 2:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(10)
#bit rate = 1760 bit/s
elif i == 3:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(9)
#bit rate = 3125 bit/s
elif i == 4:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(8)
#bit rate = 5470 bit/s
elif i == 5:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(7)
#data rate = 11000 bit/s
elif i == 6:
    lora.bandwidth(LoRa.BW_250KHZ)
    lora.sf(7)

pkt = 'PONG MODE ' + str(i)
while True:
    if s.recv(64) == b'PING':
        s.send(pkt)
        print(pkt)
    time.sleep(5)
