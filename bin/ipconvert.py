#!/usr/bin/env python

import csv
import sys
import socket
import struct

if len(sys.argv) != 3:

    print("Usage: python ipconvert.py [integer field] [string field]")
    sys.exit(1)

else:

    integerfield = sys.argv[1]
    stringfield = sys.argv[2]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    for result in r:
        if result[integerfield] and result[stringfield]:
            w.writerow(result)

        elif result[integerfield]:
            try:
                result[stringfield] = socket.inet_ntoa(struct.pack('!L', int(result[integerfield])))
            except:
                pass 
            w.writerow(result)

        elif result[stringfield]:
            try:
                result[integerfield] = struct.unpack('!L', socket.inet_aton(result[stringfield]))[0]
            except:
                pass
            w.writerow(result)
