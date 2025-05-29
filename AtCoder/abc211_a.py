from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

from decimal import Decimal


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    A, B = map(int, stdin.readline().split())
    A = Decimal(A)
    B = Decimal(B)
    C = (A - B) / 3 + B
    print(C)
    



if __name__ == "__main__":
    main()