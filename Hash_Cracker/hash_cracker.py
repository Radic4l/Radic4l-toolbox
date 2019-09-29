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

file_lenght = subprocess.Popen(callBash,stdout=subprocess.PIPE,shell=True)
wordlistLenght = file_lenght.stdout.read().decode('latin-1').replace("\n","")

with wordlst as fp:
    cnt = 0
    line = fp.readline()
    # print([i for i in line],end='\n')

    while line:
        cnt += 1
        if options.sha256:
            line_hash = hashlib.sha256(line.strip().encode()).hexdigest()
            passed_hash = options.sha256
        elif options.md5:
            line_hash = hashlib.md5(line.strip().encode()).hexdigest()
            passed_hash = options.md5
            # print([i for i in line],end='\n')
        else:
            print('Choose hash type ...')

        toto = f'Current Hash : {line_hash}/{passed_hash} ({cnt}/{wordlistLenght})'
        # input()
        if line_hash == passed_hash:
            cnt += 1
            # print('',end='\n\r')
            print(f'''
            \n{'='*int(len(toto)/2-5)}HASH  FOUND{'='*int(len(toto)/2-5)}\n{toto}\nResult Hash  : {line}
            ''')
            break
        else:
            line = fp.readline()
            # print(f'''{'='*int(len(toto)/2-5)}{'='*int(len(toto)/2-5)}''',toto,sep='',end='\r',file=sys.stdout,flush=True)
            # print(f'''\r{'='*int(len(toto)/2-5)}Progress..  {'='*int(len(toto)/2-5)}''')
            print(f'{toto}',end='\r')


        # print(wordlistLenght)
        # input('Continue ...')
# fp.close()

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
