#!/usr/bin/env python3
import os
import sys
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")

def helplk():
    print("follow the examples:")
    print("")
    print("%s -r duckduckgo.com"%(sys.argv[0]))
    print("%s -x 8.8.8.8"%(sys.argv[0]))

if len(sys.argv) <=1:
    helplk()
    sys.exit()

elif len(sys.argv) >=4:
    helplk()
    sys.exit()

def resolvelk():
    url = str(sys.argv[2])
    try:
        gt = (socket.gethostbyname(url))
        print(gt)
    except KeyboardInterrupt:
        sys.exit()
    else:
        sys.exit()
    finally:
        sys.exit()

def reverselk():
    arg = str(sys.argv[2])
    try:
        name, alias, addresslist = socket.gethostbyaddr(arg)
        gt2 = (name, alias, addresslist)
        print(gt2)
    except KeyboardInterrupt:
        sys.exit()
    else:
        sys.exit()
    finally:
        sys.exit()

choice = str(sys.argv[1])
if choice == "-r":
    if len(sys.argv) !=2:
        resolvelk()
    else:
        helplk()

elif choice == "-x":
    if len(sys.argv) !=2:
        reverselk()
    else:
        helplk()

elif choice == "-h":
    helplk()

elif choice == "--help":
    helplk()

else:
    print("ERROR, NO OPTION OR DIGITATION ERROR")
