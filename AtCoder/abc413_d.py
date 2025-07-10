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
    testcases = []
    for _ in range(T):
        N = int(stdin.readline().strip())
        A = list(map(int, stdin.readline().strip().split()))
        testcases.append(A)

    for A in testcases:
        N = len(A)
        # すべて同じ値なら Yes
        if all(a == A[0] for a in A):
            print("Yes")
            continue

        # 先頭の値とそのマイナス倍しかなく、それぞれ ceil(N/2), floor(N/2) 個なら Yes
        p = A[0]
        p_count = A.count(p)
        n_count = A.count(-p)
        if p_count + n_count == N and min(p_count, n_count) == N // 2:
            print("Yes")
            continue

        # 絶対値でソート
        A.sort(key=lambda x: abs(x))

        # Aに0は含まれないことが前提
        flag = True
        for i in range(1, len(A)-1):
            a = A[i-1]
            b = A[i]
            c = A[i+1]
            if a*c != b*b:
                flag = False
                break

        if flag:
            print("Yes")
        else:
            print("No")




if __name__ == "__main__":
    main()
