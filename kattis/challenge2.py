#!/usr/bin/env python3
from sys import stdin, stdout, stderr

def main():
    g, s, c = next(stdin).split(" ")
    g = int(g)
    s = int(s)
    c = int(c)

    value = g*3 + s *2 + c*1

    victory = {"Province or ":8, "Duchy or ":5, "Estate or ":2, "":0}
    treasure = {"Gold":6, "Silver":3, "Copper":0}

    ans = ""

    for v,c in victory.items():
        if c <=value:
            ans += v
            break

    for v,c in treasure.items():
        if c <=value:
            ans += v
            break
        
    print(ans)

if __name__ == "__main__":
    main()