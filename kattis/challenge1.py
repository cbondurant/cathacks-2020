#!/usr/bin/env python3
from sys import stdin, stdout, stderr

def main():
    x, y, n = next(stdin).split(" ")
    for i in range(1,int(n)+1):
        s = ""
        if i%int(x) == 0: s += "Fizz"
        if i%int(y) == 0: s += "Buzz"

        if s:
            print(s)
        else:
            print(i)

if __name__ == "__main__":
    main()