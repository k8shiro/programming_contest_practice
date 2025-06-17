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

    pairs = []
    import math
    max_a = float('-inf')
    for _ in range(N):
        x, y = map(int, stdin.readline().strip().split())
        x_a, y_a = x-1, y
        x_b, y_b = x, y-1
        if y_a * x_b > y_b * x_a:
            pairs.append(((x_a, y_a), (x_b, y_b)))
        else:
            pairs.append(((x_b, y_b), (x_a, y_a)))
    
    # print(pairs)
    from functools import cmp_to_key
    pairs = sorted(pairs, key=cmp_to_key(cmp))
    end_angle = (0, 1)
    count = 0
    for start, end in pairs:
        # end_angle >= start 
        if end_angle[1] * start[0] >= start[1] * end_angle[0]:
            count += 1
            end_angle = end

    print(count)


def cmp(a, b):
    # y_a/x_a > y_b/x_bを比較する
    # y_a * x_b > y_b * x_aに変形
    # print('AAAA', a, b)
    x_a, y_a = a[1]
    x_b, y_b = b[1]
    if y_a * x_b > y_b * x_a:
        return -1
    elif y_a * x_b < y_b * x_a:
        return 1
    else:
        return 0







if __name__ == "__main__":
    main()


# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# from decimal import Decimal

# # メモ化
# from functools import lru_cache

# # 探索失敗用にINT_MAXを定義
# INT_MAX = 10**18

# # 10^9 + 7
# MOD = 10**9 + 7


# def main():
#     N = int(stdin.readline().strip())

#     pairs = []
#     import math
#     max_a = float('-inf')
#     for _ in range(N):
#         x, y = map(int, stdin.readline().strip().split())
#         x_a, y_a = x-1, y
#         angle_a = math.atan2(y_a, x_a)
#         x_b, y_b = x, y-1
#         angle_b = math.atan2(y_b, x_b)
#         a, b = min(angle_a, angle_b), max(angle_a, angle_b)
#         pairs.append((a, b))
#         max_a = max(max_a, a)
    
#     print(pairs)
#     pairs = set(pairs)
#     pairs = list(pairs)
#     pairs = sorted(pairs, key=lambda x: x[1])
#     end_angle = float('-inf')
#     count = 0
#     for start, end in pairs:
#         if start >= end_angle:
#             count += 1
#             end_angle = end

#     print(count)








# if __name__ == "__main__":
#     main()
