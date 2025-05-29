from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

from decimal import Decimal


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18


def main():
    S1 = str(stdin.readline().strip())
    S2 = str(stdin.readline().strip())
    S3 = str(stdin.readline().strip())
    S4 = str(stdin.readline().strip())
    S = [S1, S2, S3, S4]
    S.sort()

    _S = ["H", "2B", "3B", "HR"]
    _S = sorted(_S)
    for i in range(4):
        if S[i] != _S[i]:
            print("No")
            return
    print("Yes")
    



if __name__ == "__main__":
    main()