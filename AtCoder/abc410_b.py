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
    N, Q = map(int, stdin.readline().strip().split())
    X = list(map(int, stdin.readline().strip().split()))
    
    BOX = [0] * N
    min_idx = 0
    min_val = 0
    ANS = []
    for x in X:
        if x == 0:
            BOX[min_idx] += 1
            ANS.append(min_idx + 1)
            min_val += 1
            for idx, b in enumerate(BOX):
                if b < min_val or (b == min_val and idx < min_idx):
                    min_val = b
                    min_idx = idx
        else:
            BOX[x-1] += 1
            ANS.append(x)
            if x - 1 == min_idx:
                min_val += 1
                for idx, b in enumerate(BOX):
                    if b < min_val or (b == min_val and idx < min_idx):
                        min_val = b
                        min_idx = idx

        #print(*BOX, '|', min_idx, min_val)
    print(*ANS)



    




if __name__ == "__main__":
    main()
