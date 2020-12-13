#!/usr/bin/env python3
from sys import stdin, stdout, stderr
from collections import defaultdict

def fibb():
    p = 0
    c = 1
    i = 1
    while True:
        yield c
        p, c = c, p+c

def main():
    next(stdin)

    for m in stdin:
        m = int(m)
        seen = {}
        for i,v in enumerate(fibb()):
            if v%m not in seen or seen[v%m]<2:
                seen[v%m] = i
            else:
                print(seen[v%m])
                break

if __name__ == "__main__":
    main()