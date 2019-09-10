# #!usr/bin/env python
# ## Hash_Cracker v0.1 written by Radic4l
import platform
import hashlib, sys
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
        break
    except all:
        print('No file found \n')
        parser.error("try again ...")

wordlst = open(wordlist, 'r', encoding='latin-1')
callBash = f"wc -l {wordlist} | cut -d ' ' -f1"

toto = subprocess.Popen(callBash,stdout=subprocess.PIPE,shell=True)
wordlistLenght = toto.stdout.read().decode('utf-8').replace("\n","")

with wordlst as fp:
    line = fp.readline()
    cnt = 1
    while line:
        # print("Line {}: {}".format(cnt, line.strip()))
        # input('Read next line ...')
        cnt += 1
        if options.sha256:
            line_hash = hashlib.sha256(line.encode('latin-1')).hexdigest()
            hash = options.sha256
        elif options.md5:
            line_hash = hashlib.md5(line.encode('latin-1')).hexdigest()
            hash = options.md5

        toto = f'Current Hash : {line_hash} \nHash tested : ({cnt}/{wordlistLenght})'
        digits = len(str(len(toto) - 1))
        delete = "\b" * (digits)
        input()
        if hash == line_hash:
            cnt += 1
            print(f'Hash FOUND : {line} || Hash : {line_hash}')
            break
        else:
            # print("{0}{1:{2}}".format(delete, toto, digits))
            print(toto, sep=' ', end='', flush=True)
            # print(toto,end='\n',flush=True)
        # sys.stdout.flush()
        line = fp.readline()  # mettre a la fin de if elif else etc ...
        # print(wordlistLenght)
        # input('Continue ...')
fp.close()

# filepath = 'rockyou.txt'

# hash_count = 0
# # wordlist = wordlist.readlines()
# wordlist = wordlist.readline()
#
#
#
# # for word in wordlist:
# #     word = word.strip('\n')
# #     if options.sha256:
# #         wordlist_hash = hashlib.sha256(word.encode('latin-1')).hexdigest()
# #         hash = options.sha256
# #     elif options.md5:
# #         wordlist_hash = hashlib.md5(word.encode('latin-1')).hexdigest()
# #         hash = options.md5
# #
# #     if hash == wordlist_hash:
# #         hash_count = hash_count + 1
# #         print('Hash FOUND : '+word+' || Hash : '+wordlist_hash)
# #         break
# #     else:
# #         hash_count = hash_count + 1
# #         print('Current Hash : '+wordlist_hash+'\nHash tested : ({0}/{1})'.format(hash_count,len(wordlist)))
# #         # if platform.system()=='Linux':
# #         #     subprocess.call('clear', shell=True)
# #         # else:
# #         #     subprocess.call('cls',shell=True)
