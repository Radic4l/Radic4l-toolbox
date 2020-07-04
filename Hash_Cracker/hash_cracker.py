#!/usr/bin/env python
## Hash_Cracker v0.1 written by Radic4l
import hashlib, subprocess, argparse

parser = argparse.ArgumentParser(description="Hash Cracker by Radic4l", prog="crack")
groupe_types =  parser.add_mutually_exclusive_group(required=True)
parser.add_argument('-w', dest='wordlist', help='Use a wordlist', required=True)
groupe_types.add_argument('--md5', dest='md5' ,help='MD5 hash type')
groupe_types.add_argument('--sha256', dest='sha256' ,help='SHA256 hash type')
groupe_types.add_argument('--sha1', dest='sha1',help='SHA1 hash type')

args = parser.parse_args()
while True:
    try:
        wordlist = args.wordlist
        wordlst = open(wordlist, 'r', encoding='latin-1')
        callBash = f"wc -l {wordlist} | cut -d ' ' -f1"
        file_lenght = subprocess.Popen(callBash, stdout=subprocess.PIPE, shell=True)
        wordlistLenght = file_lenght.stdout.read().decode('latin-1').replace("\n", "")
        break
    except BaseException:
        parser.print_help()
        break

try:
    with wordlst as fp:
        cnt = 0
        line = fp.readline()

        while line:
            cnt += 1
            if args.sha256:
                line_hash = hashlib.sha256(line.strip().encode()).hexdigest()
                passed_hash = args.sha256
            elif args.md5:
                line_hash = hashlib.md5(line.strip().encode()).hexdigest()
                passed_hash = args.md5
            elif args.sha1:
                line_hash = hashlib.sha1(line.strip().encode()).hexdigest()
                passed_hash = args.sha1

            searching = f'[!] Trying Hash ... : {line_hash} --- ({cnt}/{wordlistLenght})'
            match_found = f'[+] Hash Matching : {line_hash}/{passed_hash} ({cnt}/{wordlistLenght})'
            if line_hash == passed_hash:
                cnt += 1
                print(f'''
                \n{'=' * int(len(match_found) / 2 - 6)} HASH FOUND {'=' * int(len(match_found) / 2 - 5)}\n{match_found}\n[+] Result Hash  : {line}
                ''')
                break
            else:
                line = fp.readline()
                print(f'{searching}', end='\r')
except:
    exit()