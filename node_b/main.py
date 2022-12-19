from network import LoRa
import socket
import time

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
lora.bandwidth(LoRa.BW_125KHZ)
lora.sf(12)

while True:
    i = i + 1 if i > 5 else 1 
    i = 0 if i > 35 else 0
    if s.recv(64) == b'Ping DR 0':
        i = i + 1
        s.send('Pong DR 0')
        print('Pong DR 0')
    elif s.recv(64) == b'Ping DR 1' or (i > 5 and i <= 10):
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(11)
        s.send('Pong DR 1')
        print('Pong DR 1')
    elif s.recv(64) == b'Ping DR 2' or (i > 10 and i <= 15):
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(10)
        s.send('Pong DR 2')
        print('Pong DR 2')
    elif s.recv(64) == b'Ping DR 3' or (i > 15 and i <= 20):
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(9)
        s.send('Pong DR 3')
        print('Pong DR 3')
    elif s.recv(64) == b'Ping DR 4' or (i > 20 and i <= 25):
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(8)
        s.send('Pong DR 4')
        print('Pong DR 4')
    elif s.recv(64) == b'Ping DR 5' or (i > 25 and i <= 30):
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(7)
        s.send('Pong DR 5')
        print('Pong DR 5')
    elif s.recv(64) == b'Ping DR 6' or (i > 30 and i <= 35):
        lora.bandwidth(LoRa.BW_250KHZ)
        lora.sf(7)
        s.send('Pong DR 6')
        print('Pong DR 6')      
    time.sleep(5)
