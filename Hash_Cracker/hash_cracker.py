# #!usr/bin/env python
# ## Hash_Cracker v0.1 written by Radic4l
import hashlib
from optparse import OptionParser
import subprocess

parser = OptionParser()
parser.add_option("-w",dest="wordlist",help="Path/to/wordlist.txt")
parser.add_option("--md5",dest="md5",help="Enter your md5 hash")
parser.add_option("--sha256",dest="sha256",help="Enter your sha256 hash")
parser.add_option("--sha1",dest="sha1",help="Enter your sha1 hash")
(options, args) = parser.parse_args()

while True:
    try:
        wordlist = options.wordlist
        wordlst = open(wordlist, 'r', encoding='latin-1')
        callBash = f"wc -l {wordlist} | cut -d ' ' -f1"
        file_lenght = subprocess.Popen(callBash, stdout=subprocess.PIPE, shell=True)
        wordlistLenght = file_lenght.stdout.read().decode('latin-1').replace("\n", "")
        break
    except BaseException:
        parser.print_help()
        break

with wordlst as fp:
    cnt = 0
    line = fp.readline()

    while line:
        cnt += 1
        if options.sha256:
            line_hash = hashlib.sha256(line.strip().encode()).hexdigest()
            passed_hash = options.sha256
        elif options.md5:
            line_hash = hashlib.md5(line.strip().encode()).hexdigest()
            passed_hash = options.md5
        elif options.sha1:
            line_hash = hashlib.sha1(line.strip().encode()).hexdigest()
            passed_hash = options.sha1
        else:
            print('Choose hash type ...')

        searching = f'[!] Trying Hash ... : {line_hash} --- ({cnt}/{wordlistLenght})'
        match_found = f'[+] Hash Matching : {line_hash}/{passed_hash} ({cnt}/{wordlistLenght})'
        if line_hash == passed_hash:
            cnt += 1
            # print('',end='\n\r')
            print(f'''
            \n{'='*int(len(match_found) / 2 - 6)} HASH FOUND {'=' * int(len(match_found) / 2 - 5)}\n{match_found}\n[+] Result Hash  : {line}
            ''')
            break
        else:
            line = fp.readline()
            print(f'{searching}', end='\r')
