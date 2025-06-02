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
    L, Q = map(int, stdin.readline().strip().split())
    
    from sortedcontainers import SortedList
    sl = SortedList()
    sl.add((0, L))

    for _ in range(Q):
        c, x = map(int, stdin.readline().strip().split())
        if c == 1:  # 切る
            idx = sl.bisect_left((x, L)) - 1
            # print(idx, sl)
            l, r = sl[idx]
            sl.remove((l, r))
            sl.add((l, x))
            sl.add((x, r))
        elif c == 2:  # 長さを求める
            idx = sl.bisect_left((x, L)) - 1
            l, r = sl[idx]
            print(r - l)




if __name__ == "__main__":
    main()

# TLE
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
#     L, Q = map(int, stdin.readline().strip().split())
    
#     from collections import deque
#     queue = deque([(0, L)])

#     for _ in range(Q):
#         c, x = map(int, stdin.readline().strip().split())
#         while True:
#             left, right = queue.popleft()
            
#             # c1: 切る
#             if c == 1:
#                 if left < x < right:
#                     queue.append((left, x))
#                     queue.append((x, right))
#                     break
#                 else:
#                     queue.append((left, right))
            
#             # c2: 長さを求める
#             elif c == 2:
#                 if left < x < right:
#                     print(right - left)
#                     queue.append((left, right))
#                     break
#                 else:
#                     queue.append((left, right))


# if __name__ == "__main__":
#     main()
