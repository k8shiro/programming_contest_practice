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
    # N頂点、M辺のグラフ
    N, M = map(int, stdin.readline().strip().split())

    edges = set()
    for _ in range(M):
        # aとbの間に辺があることを示す（無向）
        a, b = map(int, stdin.readline().strip().split())
        a, b = min(a, b), max(a, b)
        edges.add((a, b))

    all_edges = [(min(a, b), max(a, b)) for a in range(1, N + 1) for b in range(a + 1, N + 1)]
    # print(all_edges)

    # 辺の数はN個にしたいので
    ANS = INT_MAX
    from itertools import combinations
    for comb in combinations(all_edges, N):
        deg = [0] * (N)
        for a, b in comb:
            deg[a - 1] += 1
            deg[b - 1] += 1
        
        
        if all(d  == 2 for d in deg): # すべての次数が2であるかを確認
            # print(edges)
            # print(comb)
            diff = set(comb) ^ edges
            ANS = min(ANS, len(diff))
    print(ANS)

if __name__ == "__main__":
    main()
