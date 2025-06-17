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
    S = str(stdin.readline().strip())

    from itertools import permutations

    s_set = set() 
    for s in permutations(S):
        s = ''.join(s)
        s_set.add(s)

    print(len(s_set))





if __name__ == "__main__":
    main()
