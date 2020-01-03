# Adapted from: https://github.com/samaaron/sonic-pi/blob/master/etc/doc/tutorial/12.1-Receiving-OSC.md


import time
import asyncio
from pythonosc import osc_message_builder
from pythonosc import udp_client
import numpy as np

SERVER_IP = '192.168.1.32'
SERVER_OSC_PORT = 4559

sender = udp_client.SimpleUDPClient(SERVER_IP, SERVER_OSC_PORT)

Z = -1

a = np.array([
    [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, Z, Z, Z, 3, Z, Z, Z, 2, Z, Z, Z, 3, Z, Z, Z],
    [4, Z, Z, Z, 5, Z, Z, Z, 4, Z, Z, Z, 5, Z, Z, Z],  #
    [Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z, Z],
], dtype='int')


def play_note(col):
    print("col", col)
    # a, b, c, d = col
    # Play A4
    sender.send_message('/trigger/prophet', [col, 0.0625])


def drummer():
    counter = Z
    time.sleep(time.time() * 8 % 1 / 8)  # enable to sync clock for demo
    n = 0
    while True:
        counter += 1
        t = counter % a.shape[1]
        col = a[:, t].tolist()
        play_note(col)
        print(counter, "->", n)
        time.sleep(.125 - time.time() * 8 % 1 / 8)


drummer()
