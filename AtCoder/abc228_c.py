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
    N, K = map(int, stdin.readline().strip().split())
    POINTS = []
    for i in range(N):
        P = map(int, stdin.readline().strip().split())
        sum_P = sum(P)
        POINTS.append((sum_P, i))

    POINTS.sort(reverse=True)
    # print(POINTS)

    ans = ['No'] * N
    for i in range(K):
        ans[POINTS[i][1]] = 'Yes'

    for i in range(K, N):
        top_k_point = POINTS[K - 1][0]
        my_point = POINTS[i][0]
        if my_point + 300 >= top_k_point or my_point + 300 >= 1200:
            ans[POINTS[i][1]] = 'Yes'
        else:
            ans[POINTS[i][1]] = 'No'

    for a in ans:
        print(a)
    

if __name__ == "__main__":
    main()
