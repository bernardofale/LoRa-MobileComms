from network import LoRa
import socket
import time
from machine import Pin
import machine


button = Pin('P10', mode = Pin.IN, pull = Pin.PULL_UP)

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

i = 0
def increment_counter(pin):
    global i
    if i == 6:
        i = 0
    else:
        i = i + 1
    print('MODE ', i)

button.callback(trigger=Pin.IRQ_FALLING, handler=increment_counter)


while True:
    if i == 0:
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(12)
    elif i == 1:
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(11)
    elif i == 2:
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(10)
    elif i == 3:
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(9)
    elif i == 4:
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(8)
    elif i == 5:
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(7)
    elif i == 6:
        lora.bandwidth(LoRa.BW_250KHZ)
        lora.sf(7)
    if s.recv(64) == b'Ping DR 0':
        s.send('Pong DR 0')
        print('Pong DR 0')
        time.sleep(5)
    elif s.recv(64) == b'Ping DR 1':
        s.send('Pong DR 1')
        print('Pong DR 1')
        time.sleep(5)
    elif s.recv(64) == b'Ping DR 2' :
        s.send('Pong DR 2')
        print('Pong DR 2')
        time.sleep(5)
    elif s.recv(64) == b'Ping DR 3' :
        s.send('Pong DR 3')
        print('Pong DR 3')
        time.sleep(5)
    elif s.recv(64) == b'Ping DR 4' :
        s.send('Pong DR 4')
        print('Pong DR 4')
        time.sleep(5)
    elif s.recv(64) == b'Ping DR 5' :
        s.send('Pong DR 5')
        print('Pong DR 5')
        time.sleep(5)
    elif s.recv(64) == b'Ping DR 6' :
        s.send('Pong DR 6')
        print('Pong DR 6')
        time.sleep(5)

def rnd_triage():
    global i
    i += 1
    print('MODE %d\n', i)
