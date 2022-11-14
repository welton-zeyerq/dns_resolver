#!/usr/bin/env python3
import os
import sys
import threading
try:
    import socket
except:
    sys.exit("Install missing library: pip install sockets")

def helplk():
    print("follow the examples:")
    print("")
    print("%s -r duckduckgo.com"%(sys.argv[0]))
    print("%s --resolve duckduckgo.com"%(sys.argv[0]))
    print("%s -u duckduckgo.com"%(sys.argv[0]))
    print("%s --url duckduckgo.com"%(sys.argv[0]))
    print("%s -x 8.8.8.8"%(sys.argv[0]))
    print("%s --reverse 8.8.8.8"%(sys.argv[0]))

if len(sys.argv) <=1:
    helplk()
    sys.exit()

if len(sys.argv) >=4:
    helplk()
    sys.exit()

def resolvelk():
    try:
        url = str(sys.argv[2])
        gt = (socket.gethostbyname(url))
        print(gt)
    except socket.gaierror:
        print("socket error")
        pass

def reverselk():
    try:
        arg = str(sys.argv[2])
        name, alias, addresslist = socket.gethostbyaddr(arg)
        gt2 = (name, alias, addresslist)
        print(gt2)
    except socket.gaierror:
        print("socket error")
        pass

def threads_resolve():
    try:
        THREADS = []
        for i in range(1):
            t = threading.Thread(target=resolvelk)
            THREADS.append(t)
        for t in THREADS:
            t.start()
            t.join()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as error:
        print(error)

def threads_reverse():
    try:
        THREADS = []
        for i in range(1):
            t = threading.Thread(target=reverselk)
            THREADS.append(t)
        for t in THREADS:
            t.start()
            t.join()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    try:
        choice = str(sys.argv[1])
        if choice == "-h":
            helplk()
        elif choice == "--help":
            helplk()
        elif choice == "-r":
            if len(sys.argv) !=2:
                threads_resolve()
            else:
                helplk()
        elif choice == "-u":
            if len(sys.argv) !=2:
                threads_resolve()
            else:
                helplk()
        elif choice == "--url":
            if len(sys.argv) !=2:
                threads_resolve()
            else:
                helplk()
        elif choice == "--resolve":
            if len(sys.argv) !=2:
                threads_resolve()
            else:
                helplk()
        elif choice == "-x":
            if len(sys.argv) !=2:
                threads_reverse()
            else:
                helplk()
        elif choice == "--reverse":
            if len(sys.argv) !=2:
                threads_reverse()
            else:
                helplk()
        else:
            print("ERROR, NO OPTION OR DIGITATION ERROR")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as error:
        print(error)
        sys.exit()
