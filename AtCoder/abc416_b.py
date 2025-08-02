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
    T = ['.'] * len(S)
    flag = True
    for i in range(len(S)):
        if S[i] == '#':
            T[i] = '#'
            flag = True
        elif S[i] == '.' and flag:
            T[i] = 'o'
            flag = False
        else:
            T[i] = '.'

    print(''.join(T))




if __name__ == "__main__":
    main()
