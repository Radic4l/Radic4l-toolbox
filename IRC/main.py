#!/usr/bin/env python
# -*- coding: utf-8 -*-
import irc3,socket, struct

HOST = 'irc.root-me.org'
PORT = 6667
ADDRESS = (HOST,PORT)
CHANNEL = '#root-me_challenge'
BOTNAME = 'candy'


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
input(f'[+] Connecting to irc {HOST}')
soc.connect((HOST,PORT))
input('OK ! Sending simply packet ...')
packet = struct.pack('!B', 0)
soc.sendto(packet,ADDRESS)
print('Message Sent ! Try to receive ...')
data,_ = soc.recvfrom(1024)
input('Received message !')
print(f'DATA : {data}')
