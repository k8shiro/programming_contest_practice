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
    N = int(stdin.readline().strip())
    
    AB = []
    for _ in range(N):
        a, b = map(int, stdin.readline().strip().split())
        AB.append((Decimal(a), Decimal(b)))

    end_time = Decimal(0)
    for a, b in AB:
        end_time += a / b
    end_time = end_time / Decimal(2)

    past_time = Decimal(0)
    past_length = Decimal(0)
    for a, b in AB:
        if past_time + a / b < end_time:
            past_time += a / b
            past_length += a
            continue

        rest_time = end_time - past_time
        rest_length = b * rest_time
        past_length += rest_length
        break

    print(past_length)


    

    

    




if __name__ == "__main__":
    main()
