from network import LoRa
import socket
import time
from machine import Pin


# This is the code for NODE B

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

i = 0
if i == 0:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(12)
elif i == 1:
    lora.bandwidth(LoRa.BW_500KHZ)
    lora.sf(12)
elif i == 2:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(10)
elif i == 3:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(8)
elif i == 4:
    lora.bandwidth(LoRa.BW_500KHZ)
    lora.sf(11)
elif i == 5:
    lora.bandwidth(LoRa.BW_250KHZ)
    lora.sf(9)
elif i == 6:
    lora.bandwidth(LoRa.BW_125KHZ)
    lora.sf(7)

while True:
    if s.recv(64) == b'PING':
        s.send('ACK')
        print('ACK')
    time.sleep(5)
