#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,socket

HOST = 'irc.root-me.org'
PORT = 6667
ADDRESS = (HOST,PORT)
BOTNAME = 'candy'

# Commande Chall

def send_data(command):
    soc.send(command)


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f'[+] Connecting to irc {HOST}')
soc.connect((HOST,PORT))
print('[i] Login ...')
send_data(b'USER titi tutu tyty :tete \r\n')
time.sleep(5)
print('[+] Create Nick ...')
send_data(b'NICK titi \r\n')
time.sleep(5)
print('[i] Connecting to channel ...')
send_data(b'JOIN #root-me_challenge \r\n')
time.sleep(5)
send_data(b':titi JOIN #root-me_challenge \r\n')


def recv_all(sock):
    BUFF_SIZE = 1024
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            break
    return data


def get_chall1():
    import math as m
    print('[i] Intializing challenge 1 ...\n[+] Sending private message to Candy ...')
    time.sleep(3)
    send_data(b'PRIVMSG Candy !ep1 \r\n')
    msg = recv_all(soc)
    if b'Candy' in msg:
        splited = msg.decode().replace(':', '').split()
        numbers = []
        for w in splited:
            try:
                numbers.append(int(w))
            except:
                pass
        res_calcul = round(m.sqrt(numbers[0]) * numbers[1], 2)
        rep = f'PRIVMSG Candy !ep1 -rep {res_calcul} \r\n'
        send_data(rep.encode('ascii'))
    else:
        print('[!] No response from bot Candy')


def get_chall2():
    import base64
    print('[i] Intializing challenge 2 ...\n[+] Sending private message to Candy ...')
    time.sleep(3)
    send_data(b'PRIVMSG Candy !ep2 \r\n')
    msg = recv_all(soc)
    if b'Candy' in msg:
        splited = msg.decode().replace(':', '').split()
        rep = f'PRIVMSG Candy !ep2 -rep {base64.b64decode(splited[-1]).decode()} \r\n'
        send_data(rep.encode('ascii'))
    else:
        print('[!] No response from bot Candy')


def get_chall3():
    import codecs as c
    print('[i] Intializing challenge 3 ...\n[+] Sending private message to Candy ...')
    time.sleep(3)
    send_data(b'PRIVMSG Candy !ep3 \r\n')
    msg = recv_all(soc)
    if b'Candy' in msg:
        splited = msg.decode().replace(':', '').split()
        rep = f'PRIVMSG Candy !ep3 -rep {c.decode(splited[-1],"rot_13")} \r\n'
        send_data(rep.encode('ascii'))
    else:
        print('[!] No response from bot Candy')


def get_chall4():
    import codecs as c,base64
    print('[i] Intializing challenge 4 ...\n[+] Sending private message to Candy ...')
    time.sleep(3)
    send_data(b'PRIVMSG Candy !ep4 \r\n')
    msg = recv_all(soc)
    if b'Candy' in msg:
        print(msg)
        splited = msg.decode().replace(':', '').split()
        print(splited)
        convert = c.decode(base64.b64decode(splited[-1]), "zlib")
        to_str = convert.decode()
        rep = f'PRIVMSG Candy !ep4 -rep {to_str} \r\n'
        print(rep)
        send_data(rep.encode('ascii'))
    else:
        print('[!] No response from bot Candy')


while True:
    data = recv_all(soc)
    print(data.decode())
    user_in = input('COMMAND => ')
    if user_in == 'chall1':
        get_chall1()
    elif user_in == 'chall2':
        get_chall2()
    elif user_in == 'chall3':
        get_chall3()
    elif user_in == 'chall4':
        get_chall4()
    elif user_in == 'quit':
        soc.close()
        exit()
    else:
        command = user_in + ' \r\n'
        send_data(command.encode('ascii'))