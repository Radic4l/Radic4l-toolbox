#!usr/bin/env python
## Hash_Cracker v0.1 written by Radic4l

import hashlib

while True:
    try:
        wordlist = input('File path containing the Wordlist : ')
        wordlist = open(wordlist,'r',encoding='latin-1')
        hash = input('Enter your sha256 hash : ')
        break
    except:
        print('No file found \n')

for word in wordlist.readlines():
    word = word.strip('\n')
    wordlist_hash=hashlib.sha224(word.encode('latin-1')).hexdigest()
    if(hash==wordlist_hash):
        print('Hash FOUND : '+word+' || Hash : '+wordlist_hash)
        break
    else:
        print('No correspondence for this hash : '+wordlist_hash)
            
