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
    N, M = map(int, stdin.readline().strip().split())
    B = []
    for _ in range(N):
        b = list(map(int, stdin.readline().strip().split()))
        B.append(b)
    
    # 左上が (i - 1) * 7 + jを満たすか
    flag = False
    for j in range(1, 7-M+1+1):
        if (B[0][0] - j) % 7 != 0:
            continue
        flag = True
        #i = (B[0][0] - j) // 7 + 1
        
        # 高さの判定がいるような気がするが一旦無視
    if flag is False:
        print("No")
        return


    # B11 + 7 == B21 をチェック
    for i in range(N-1):
        for j in range(M):
            if B[i][j] + 7 != B[i+1][j]:
                print("No")
                return

    # B11 + 1 == B12 をチェック
    for i in range(N):
        for j in range(M-1):
            if B[i][j] + 1 != B[i][j+1]:
                print("No")
                return

    print("Yes")






if __name__ == "__main__":
    main()
