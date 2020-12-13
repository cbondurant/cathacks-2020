#!/usr/bin/env python3
from sys import stdin, stdout, stderr

def main():
    c = 0
    for l in stdin:
        c += 1
        e, m = l.split(" ")
        e = int(e)
        m = int(m)

        d = 0
        while not (e==m==0):
            e = (e+1) % 365
            m = (m+1) % 687
            d += 1 

        print("Case {}:".format(c), d)

if __name__ == "__main__":
    main()