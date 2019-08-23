#!usr/bin/env python
## Hash_Cracker v0.1 written by Radic4l
import platform
import hashlib
from optparse import OptionParser
import subprocess

parser = OptionParser('''
        [Options]:

        -w :        wordlist
        --sha256 :  option for sha256
        --md5 :     option for md5 

        Exemple : python hash_cracker.py -w rockyou.txt --sha256 <hash>
        ''')

parser.add_option("-w",dest="wordlist",help="Path/to/wordlist.txt")
parser.add_option("--md5",dest="md5",help="Enter your md5 hash")
parser.add_option("--sha256",dest="sha256",help="Enter your sha256 hash")

while True:
    try:
        (options, args) = parser.parse_args()
        wordlist = options.wordlist
        wordlist = open(wordlist,'r',encoding='latin-1')
        break
    except all:
        #print('No file found \n')
        parser.error("try again ...")
        parser.print_help

hash_count = 0
wordlist = wordlist.readlines()

for word in wordlist:
    word = word.strip('\n')
    if options.sha256:
        wordlist_hash = hashlib.sha256(word.encode('latin-1')).hexdigest()
        hash = options.sha256
    elif options.md5:
        wordlist_hash = hashlib.md5(word.encode('latin-1')).hexdigest()
        hash = options.md5

    if hash == wordlist_hash:
        hash_count = hash_count + 1
        print('Hash FOUND : '+word+' || Hash : '+wordlist_hash)
        break
    else:
        hash_count = hash_count + 1
        print('Current Hash : '+wordlist_hash+'\nHash tested : ({0}/{1})'.format(hash_count,len(wordlist)))
        # if platform.system()=='Linux':
        #     subprocess.call('clear', shell=True)
        # else:
        #     subprocess.call('cls',shell=True)
