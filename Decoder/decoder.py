import base64
from optparse import OptionParser
import subprocess

parser = OptionParser('''
        [Options]:
        
        -b : base64 decode
        
        Exemple : python decoder.py -b <base64>
        ''')

parser.add_option("-b",dest="code",help="Enter your base64 code")

try:
    (options,args)= parser.parse_args()
    code = options.code
    decode_code = base64.b64decode(code)
    subprocess.call('clear',shell=True)
    print(decode_code)
except:
    parser.error("Read Help")
