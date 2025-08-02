from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

from decimal import Decimal

# メモ化
from functools import lru_cache

# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18

# 10^9 + 7
MOD = 10**9 + 7

from collections import deque

def bfs(start, n, graph):
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    return dist

def all_pair_distances(n, graph):

    all_dist = []
    for i in range(n):
        all_dist.append(bfs(i, n, graph))
    return all_dist

def main():
    T = int(stdin.readline().strip())    
    for _ in range(T):
        line = stdin.readline()
        if not line: break
        N, K = map(int, line.strip().split())

        graph = [[] for _ in range(N)]
        for _ in range(N-1):
            line = stdin.readline()
            if not line: break
            u, v = map(int, line.strip().split())
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)


        all_dist = all_pair_distances(N, graph)


        moves = [-1] * N
        q = deque()

        moves[0] = 0
        q.append(0)

        while q:
            u = q.popleft()

            for v in range(N):
                if all_dist[u][v] == K:

                    if moves[v] == -1:
                        moves[v] = moves[u] + 1
                        q.append(v)

        result = []
        for i in range(1, N):
            result.append(str(moves[i]))
        
        print(" ".join(result))

if __name__ == "__main__":
    main()