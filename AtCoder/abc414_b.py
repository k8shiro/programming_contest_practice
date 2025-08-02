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
    N = int(stdin.readline().strip())
    ans_s = []
    ans_n = 0
    query = []
    for _ in range(N):
        c, l = map(str, stdin.readline().split())
        l = int(l)
        query.append((c, l))
        # for _ in range(l):
        #     ans_s.append(c)
        ans_n += l

    if ans_n > 100:
        print('Too Long')
    else:
        ans = ''
        for c, l in query:
            ans += c * l
        print(ans)

    


if __name__ == "__main__":
    main()
