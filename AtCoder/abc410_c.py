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
    N, Q = map(int, stdin.readline().strip().split())

    A = [i for i in range(1, N + 1)]
    top_idx = 0

    for _ in range(Q):
        query = list(map(int, stdin.readline().strip().split()))
        if query[0] == 1:
            # Apをxにする
            a_idx, x = query[1], query[2]
            a_idx = (a_idx - 1 + top_idx) % N
            A[a_idx] = x

        elif query[0] == 2:
            a_idx = query[1]
            a_idx = (a_idx - 1 + top_idx) % N
            print(A[a_idx])
        elif query[0] == 3:
            k = query[1]
            top_idx = (top_idx + k) % N
        #print(*A[top_idx:], *A[:top_idx])


    




if __name__ == "__main__":
    main()
