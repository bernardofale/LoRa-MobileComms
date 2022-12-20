from network import LoRa
import socket
from utime import ticks_us, ticks_diff, sleep

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
lora.bandwidth(LoRa.BW_125KHZ)
lora.sf(12)
while True:
    #Data rate = 250 bit/s
    if i <= 5:
        t = ticks_us()
        # make the socket blocking
        s.setblocking(True)
        s.send('Ping DR 0')
        print('PING DR 0')
        s.setblocking(False)
        # print time
        delta = ticks_diff(ticks_us(), t)
        print("Sent. TX Time =", delta/1000)
        i = i + 1
        # get any data received (if any...)
        data = s.recv(64)
        print("Received:", data)
        # print stats of last packet
        print("Stats:", lora.stats())
        print("\n")
        # wait
        sleep(5)
    #data rate = 440 bit/s
    elif i > 5 and i <= 10:
        t = ticks_us()
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(11)
        # make the socket blocking
        s.setblocking(True)
        s.send('Ping DR 1')
        print('PING DR 1')
        s.setblocking(False)
        # print time
        delta = ticks_diff(ticks_us(), t)
        print("Sent. TX Time =", delta/1000)
        i = i + 1
        # get any data received (if any...)
        data = s.recv(64)
        print("Received:", data)
        # print stats of last packet
        print("Stats:", lora.stats())
        print("\n")
        # wait
        sleep(5)
    #data rate = 980 bit/s
    elif i > 10 and i <= 15:
        t = ticks_us()
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(10)
        # make the socket blocking
        s.setblocking(True)
        s.send('Ping DR 2')
        print('PING DR 2')
        s.setblocking(False)
        # print time
        delta = ticks_diff(ticks_us(), t)
        print("Sent. TX Time =", delta/1000)
        i = i + 1
        # get any data received (if any...)
        data = s.recv(64)
        print("Received:", data)
        # print stats of last packet
        print("Stats:", lora.stats())
        print("\n")
        # wait
        sleep(5)
    #data rate = 1760 bit/s
    elif i > 15 and i <= 20:
        t = ticks_us()
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(9)
        # make the socket blocking
        s.setblocking(True)
        s.send('Ping DR 3')
        print('PING DR 3')
        s.setblocking(False)
        # print time
        delta = ticks_diff(ticks_us(), t)
        print("Sent. TX Time =", delta/1000)
        i = i + 1
        # get any data received (if any...)
        data = s.recv(64)
        print("Received:", data)
        # print stats of last packet
        print("Stats:", lora.stats())
        print("\n")
        # wait
        sleep(5)
    #data rate = 3125 bit/s
    elif i > 20 and i <= 25:
        t = ticks_us()
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(8)
        # make the socket blocking
        s.setblocking(True)
        s.send('Ping DR 4')
        print('PING DR 4')
        s.setblocking(False)
        # print time
        delta = ticks_diff(ticks_us(), t)
        print("Sent. TX Time =", delta/1000)
        i = i + 1
        # get any data received (if any...)
        data = s.recv(64)
        print("Received:", data)
        # print stats of last packet
        print("Stats:", lora.stats())
        print("\n")
        # wait
        sleep(5)
    #data rate = 5470 bit/s
    elif i > 25 and i <= 30:
        t = ticks_us()
        lora.bandwidth(LoRa.BW_125KHZ)
        lora.sf(7)
        # make the socket blocking
        s.setblocking(True)
        s.send('Ping DR 5')
        print('PING DR 5')
        s.setblocking(False)
        # print time
        delta = ticks_diff(ticks_us(), t)
        print("Sent. TX Time =", delta/1000)
        i = i + 1
        # get any data received (if any...)
        data = s.recv(64)
        print("Received:", data)
        # print stats of last packet
        print("Stats:", lora.stats())
        print("\n")
        # wait
        sleep(5)
    #data rate = 11000 bit/s
    elif i > 30 and i <= 35:
        t = ticks_us()
        lora.bandwidth(LoRa.BW_250KHZ)
        lora.sf(7)
        # make the socket blocking
        s.setblocking(True)
        s.send('Ping DR 6')
        print('PING DR 6')
        s.setblocking(False)
        # print time
        delta = ticks_diff(ticks_us(), t)
        print("Sent. TX Time =", delta/1000)
        i = i + 1
        # get any data received (if any...)
        data = s.recv(64)
        print("Received:", data)
        # print stats of last packet
        print("Stats:", lora.stats())
        print("\n")
        # wait
        sleep(5)
    else:
        i = 0
