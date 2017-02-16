#!/usr/bin/env python

import csv
import sys
import socket
import struct

def main():
    if len(sys.argv) != 3:
        print "Usage: python ipconvert.py [integer field] [string field]"
        sys.exit(1)

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
            result[stringfield] = socket.inet_ntoa(struct.pack('!L', int(result[integerfield])))
            w.writerow(result)

        elif result[stringfield]:
            result[integerfield] = struct.unpack('!L', socket.inet_aton(result[stringfield]))[0]
            w.writerow(result)

main()
