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

    NEXT_NUM = {
        '0': '1',
        '1': '2',
        '2': '3',
        '3': '4',
        '4': '5',
        '5': '6',
        '6': '7',
        '7': '8',
        '8': '9',
        '9': '0'
    }

    X0 = X[0]
    X1 = X[1]
    X2 = X[2]
    X3 = X[3]

    if X0 == X1 == X2 == X3:
        print('Weak')
        return
    if NEXT_NUM[X0] == X1 and NEXT_NUM[X1] == X2 and NEXT_NUM[X2] == X3:
        print('Weak')
        return
    print('Strong')





if __name__ == "__main__":
    main()
