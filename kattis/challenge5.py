#!/usr/bin/env python3
from sys import stdin, stdout, stderr

def main():
    h, w, kh, kw = list(map(int, next(stdin).split(" ")))

    im = []
    for i in range(h):
        im.append(list(map(int, next(stdin).split(" "))))
        
    kernel = []
    for i in range(kh):
        kernel.append(list(map(int, reversed(next(stdin).split(" ")))))
    kernel.reverse()

    ans = []
    for y in range(h - kh + 1):
        row = []
        for x in range(w - kw+1):
            i = 0
            for ky, kr in enumerate(kernel):
                for kx, kv in enumerate(kr):
                    i += kv * im[y+ky][x+kx]
            row.append(i)
        ans.append(row)

    for row in ans:
        print(*row)

if __name__ == "__main__":
    main()