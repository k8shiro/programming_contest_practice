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
    X, Y, A, B, C = map(int, stdin.readline().strip().split())

    X, Y = min(X, Y), max(X, Y) # Xのほうが小さくする

    if X * Y < A + B + C:
        print("No")
        return

    flag = False
    flag = flag or check(A, B, C, X, Y)
    flag = flag or check(A, C, B, X, Y)
    flag = flag or check(B, C, A, X, Y)
    flag = flag or check(B, A, C, X, Y)
    flag = flag or check(C, A, B, X, Y)
    flag = flag or check(C, B, A, X, Y)
    
    flag = flag or check(A, B, C, Y, X)
    flag = flag or check(A, C, B, Y, X)
    flag = flag or check(B, C, A, Y, X)
    flag = flag or check(B, A, C, Y, X)
    flag = flag or check(C, A, B, Y, X)
    flag = flag or check(C, B, A, Y, X)

    flag = flag or check2(A, B, C, X, Y)
    if flag:
        print("Yes")
    else:
        print("No")

# 上下*縦置きチェック
import math
def check(A, B, C, X, Y):
    left = math.ceil(A / Y)
    right = X
    while left < right:
        mid = (left + right + 1) // 2

        mid_y = math.ceil(A / mid)

        _B = mid * (Y - mid_y)
        _C = (X - mid) * Y
        
        if _B >= B and _C >= C:
            return True
        elif _B < B and _C >= C:
            left = mid
        else:
            right = mid - 1

    return False

# 縦・横置きチェック
def check2(A, B, C, X, Y):
    AY = math.ceil(A / X)
    BY = math.ceil(B / X)
    CY = math.ceil(C / X)
    if AY + BY + CY <= Y:
        return True

    AX = math.ceil(A / Y)
    BX = math.ceil(B / Y)
    CX = math.ceil(C / Y)
    if AX + BX + CX <= X:
        return True

    return False





if __name__ == "__main__":
    main()
