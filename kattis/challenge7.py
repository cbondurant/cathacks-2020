#!/usr/bin/env python3
from sys import stdin, stdout, stderr

def main():
    pos = [0,0]
    visited = set()
    visited.add((pos[0], pos[1]))

    minx, miny = pos
    maxx, maxy = pos

    for move in stdin:
        move = move.strip()
        if move == "up":
            pos[1] -= 1
        if move == "down":
            pos[1] += 1
        if move == "right":
            pos[0] += 1
        if move == "left":
            pos[0] -= 1
        visited.add((pos[0], pos[1]))
        minx = min(pos[0], minx)
        miny = min(pos[1], miny)
        maxx = max(pos[0], maxx)
        maxy = max(pos[1], maxy)

    lines = []
    for y in range(miny-1, maxy+2):
        row = ""
        for x in range(minx-1, maxx+2):
            if x< minx or maxx < x or y < miny or maxy < y:
                row += "#"
            elif x == 0 and y == 0:
                row += "S"
            elif x == pos[0] and y == pos[1]:
                row += "E"
            elif (x,y) in visited:
                row += "*"
            else:
                row += " "
        lines.append(row)

    for l in lines:
        print(l)

if __name__ == "__main__":
    main()