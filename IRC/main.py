#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,socket

HOST = 'irc.root-me.org'
PORT = 6667
ADDRESS = (HOST,PORT)
BOTNAME = 'candy'

def send_data(command):
    soc.send(command)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
input(f'[+] Connecting to irc {HOST}')
soc.connect((HOST,PORT))
input('Enter for sent ID')
send_data(b'USER titi tutu tyty :tete \r\n')
time.sleep(5)
send_data(b'NICK titi \r\n')
time.sleep(5)
send_data(b'JOIN #root-me_challenge \r\n')
time.sleep(5)
send_data(b':titi JOIN #root-me_challenge \r\n')
data= soc.recv(1024).decode()
print(data)

while data:
    data = soc.recv(1024).decode()
    print(data)

# try:
#     soc.connect((HOST,PORT))
#     print(f'[Connected to {HOST}')
#     try:
