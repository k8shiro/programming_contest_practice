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

    ANS = ''
    while N != 0:
        if N % 2 == 1:
            N -= 1
            ANS += 'A'
        else:
            N //= 2
            ANS += 'B'
    ANS = ANS[::-1]  # 逆順にする
    print(ANS)



if __name__ == "__main__":
    main()

# def main():
#     N = int(stdin.readline().strip())

#     from mpmath import mp
#     mp.dps = 100
#     log2n = mp.log(N, 2)
#     # print(f'mpmathでのlog2(N) = {log2n}')
#     b_num = int(log2n)

#     ball_num = 2 ** b_num
#     a_num = N - ball_num

#     # 最初に1回 A
#     # 次に b_num 回 B
#     # 最後に a_num 回 A
#     result = "A" + "B" * b_num + "A" * a_num
#     print(result)


# if __name__ == "__main__":
#     main()
