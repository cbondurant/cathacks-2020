#!/usr/bin/env python3
from sys import stdin, stdout, stderr
from math import pi

def main():
    next(stdin)
    for i in stdin:
        radStart, iters = list(map(int, i.split(" ")))
        if iters == 1:
            print((radStart**2)*pi)
        elif iters == 2:
            print((radStart**2)*pi + ((radStart/2)**2)*4*pi)
        else:
            iters = iters - 2
            area = (radStart**2)*pi + ((radStart/2)**2)*4*pi
            curRad = radStart/4
            curCirc = 12
            for _ in range(iters):
                area += ((curRad**2)*curCirc)*pi
                curRad /= 2
                curCirc *= 3
            print(area)


if __name__ == "__main__":
    main()