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
    Q = int(stdin.readline().strip())
    queries = []
    for i in range(Q):
        t, x = map(int, stdin.readline().strip().split())
        queries.append((t, x))

    N = 2 ** 20
    A = [-1] * N
    
    from sortedcontainers import SortedList
    A_rest = SortedList(range(N))

    for t, x in queries:
        if t == 1:
            h = x % N
            i = A_rest.bisect_left(h)
            if i < len(A_rest):
                _h = A_rest[i]
                #print(_h, x)
                A[_h] = x
                A_rest.remove(_h)
            else:
                h = 0
                i = A_rest.bisect_left(h)
                _h = A_rest[i]
                #print(_h, x)
                A[_h] = x
                A_rest.remove(_h)

        if t == 2:
            h = x % N
            print(A[h])


if __name__ == "__main__":
    main()
