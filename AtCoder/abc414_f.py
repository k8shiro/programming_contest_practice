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


def main():
    T = int(stdin.readline().strip())
    for _ in range(T):
        N, K = map(int, stdin.readline().strip().split())

        edges = []
        for _ in range(N-1):
            u, v = map(int, stdin.readline().strip().split())
            u -= 1
            v -= 1
            edges.append((u, v))

        graph = [[] for _ in range(N)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        all_dist = all_pair_distances(N, graph)

        # default dict
        from collections import defaultdict
        dist_dict = defaultdict(list)
        for i, row in enumerate(all_dist):
            for j, r in enumerate(row):
                dist_dict[(i, r)].append(j)
        print(dist_dict)

        # TODO
        # 頂点0から初めて距離Kの頂点に移動する操作を繰り返す
        # 頂点 k に移動することができるかどうか判定し、移動できるならば操作回数の最小値を求める
        # 移動することができないならば -1 とする
        # ans2 ans3 ... ansNのように出力する
        for k in range(2, N+1):


 

                

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
    


if __name__ == "__main__":
    main()
