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

    count = 0
    for a in range(1, N + 1):
        if a*a*a > N:
            break
        for b in range(a, N + 1):
            c_min = b
            if a * b * c_min > N:
                break
            else:
                c_max = N // (a * b)
                # print(a, b, c_min, c_max)
                count += (c_max - c_min + 1)
    print(count)


if __name__ == "__main__":
    main()

# たぶんTLE
# def main():
#     N = int(stdin.readline().strip())

#     count = 0
#     for a in range(1, N + 1):
#         for b in range(a, N + 1):
#             c_min = b
#             if a * b * c_min > N:
#                 break
#             else:
#                 c_max = N // (a * b)
#                 # print(a, b, c_min, c_max)
#                 count += (c_max - c_min + 1)
#     print(count)





# if __name__ == "__main__":
#     main()
