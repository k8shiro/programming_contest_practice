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
    K = int(stdin.readline().strip())

    left = 0
    count_dot = 0
    ans = 0

    for right in range(len(S)):
        if S[right] == '.':
            count_dot += 1
        
        # K を超えたら左を縮める
        while count_dot > K:
            if S[left] == '.':
                count_dot -= 1
            left += 1
        
        ans = max(ans, right - left + 1)

    print(ans)
        


if __name__ == "__main__":
    main()
