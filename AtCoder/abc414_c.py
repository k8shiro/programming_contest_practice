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
    A = int(stdin.readline().strip())
    N = int(stdin.readline().strip())

    kaibun = kaibun_10(N)
    ans = 0
    for n in kaibun:
        if check_A(n, A):
           ans += n
    print(ans) 

def check_A(N, A):
    digits = []

    while N > 0:
        digits.append(N % A)
        N //= A
    return digits == digits[::-1]
    
def kaibun_10(N):
    res = []
    max_len = len(str(N))

    for d in range(1, max_len + 1):
        h = (d + 1) // 2
        s = 10 ** (h - 1) if h > 1 else 1
        e = 10 ** h

        for i in range(s, e):
            t = str(i)

            if d % 2 == 1:
                r = t[:-1][::-1]
                p = int(t + r)
            else:
                r = t[::-1]
                p = int(t + r)

            if p > N:
                return res

            res.append(p)

    return res



if __name__ == "__main__":
    main()
