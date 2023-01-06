from network import LoRa
import socket
from utime import ticks_us, ticks_diff, sleep

# This is the code for NODE A

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
#lora.tx_power(2)

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
    lora.bandwidth(LoRa.BW_250KHZ)
    lora.sf(7)

while True:
    t = ticks_us()
    # make the socket blocking
    s.setblocking(True)
    s.send('PING')
    s.setblocking(False)
    # print time
    delta = ticks_diff(ticks_us(), t)
    print("Sent. TX Time =", delta/1000)
    # get any data received (if any...)
    data = s.recv(64)
    #if data == b'ACK':
        #break
    print("Received:", data)
    # print stats of last packet
    print("Stats:", lora.stats())
    print("\n")
    # wait
    sleep(5)
