#!/usr/bin/env python3
from sys import stdin, stdout, stderr
from collections import defaultdict
from copy import deepcopy

def bfs(start, end, tree, graph):
    if start == end:
        return []

    unvisited = [start]
    visited = set()
    while unvisited:
        cur = unvisited.pop()
        for node in graph[cur].keys():
            if node not in visited:
                visited.add(node)
                unvisited.append(node)
                tree[node] = cur

    return end in visited

def max_flow(start, end, graph):
    tree = {}
    flow = 0

    while bfs(start, end, tree, graph):
        p_flow = 1000000000000 # may as well be inifinty
        s = end
        while s != start:
            parent = tree[s]
            p_flow = min(p_flow, graph[parent][s])
            s = tree[s]
        
        flow += p_flow

        s = end
        while s != start:
            parent = tree[s]
            graph[parent][s] -= p_flow
            graph[s][parent] += p_flow
            s = parent
            
    return flow

def main():
    n, p, k = list(map(int, next(stdin).split(" ")))

    graph = defaultdict(lambda: defaultdict(int))
    for i in range(p):
        a, b, c = list(map(int, next(stdin).split(" ")))
        graph[a][b] = c
        graph[b][a] = c

    print(max_flow(1,2,deepcopy(graph)))

    for i in range(k):
        a, b, c = list(map(int, next(stdin).split(" ")))
        graph[a][b] += c
        graph[b][a] += c
        print(max_flow(1,2,deepcopy(graph)))

    print(ans)

if __name__ == "__main__":
    main()