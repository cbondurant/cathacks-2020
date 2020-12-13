#!/usr/bin/env python3
from sys import stdin, stdout, stderr

def main():
    c = next(stdin)
    k = next(stdin)
    letOffset = ord("A") 
    c = [ord(l) - letOffset for l in c]
    k = [ord(l) - letOffset for l in k]

    ans = ""
    sub = True
    for lc, lk in zip(c,k):
        if sub:
            ans += chr(letOffset+ (lc-lk)%26)
        else:
            ans += chr(letOffset+ (lc+lk)%26)
        sub = not sub

    print(ans[:-1])

if __name__ == "__main__":
    main()