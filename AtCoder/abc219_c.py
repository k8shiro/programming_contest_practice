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
    X = str(stdin.readline().strip())
    N = int(stdin.readline().strip())

    X_DICT = { x: chr(ord('a') + i) for i, x in enumerate(X) }
    X_DICT_REV = { v: k for k, v in X_DICT.items() }
    # print(X_DICT)

    S = []
    for _ in range(N):
        s = str(stdin.readline().strip())
        _s = ''
        for c in s:
            _s += X_DICT[c]
        S.append(_s)

    S.sort()
    _S = []
    for s in S:
        _s = ''
        for c in s:
            _s += X_DICT_REV[c]
        _S.append(_s)
    print('\n'.join(_S))




if __name__ == "__main__":
    main()
