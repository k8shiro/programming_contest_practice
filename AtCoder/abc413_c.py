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



from collections import deque

def main():
    Q = int(stdin.readline().strip())
    queries = []
    for _ in range(Q):
        query = list(map(int, stdin.readline().strip().split()))
        queries.append(query)

    A = deque()
    for query in queries:

        if query[0] == 1:
            c, x = query[1], query[2]
            A.append((c, x))

        elif query[0] == 2:
            k = query[1]
            ans = 0
            while k > 0:
                c, x = A[0]
                take = min(k, c)
                ans += take * x
                k -= take
                if take == c:
                    A.popleft()
                else:
                    A[0] = (c - take, x)
            print(ans)

if __name__ == "__main__":
    main()

# def main():
#     Q = int(stdin.readline().strip())
#     queries = []
#     for _ in range(Q):
#         query = list(map(int, stdin.readline().strip().split()))
#         queries.append(query)

#     A = []
#     A_top = 0
#     left = 0
#     right = 0

#     for query in queries:
#         if query[0] == 1:
#             c = query[1]
#             x = query[2]

#             A.append(
#                 (right, right + c - 1, x)
#             )
#             right += c

#         elif query[0] == 2:
#             k = query[1]
#             _right = left + k -1
#             ans = 0
#             for l, r, x in A[A_top:]:
#                 if l <= left <= _right <= r:
#                     ans += k * x
#                 elif left <= l <= r <= _right:
#                     ans += (r - l + 1) * x
#                 elif l <= left <= r <= _right:
#                     ans += (r - left + 1) * x
#                 elif left <= l <= _right <= r:
#                     ans += (_right - l + 1) * x
#                 elif r < left:
#                     A_top += 1
#                     continue
#                 elif _right < l:
#                     break
#             print(ans)
#             left += k

    

# if __name__ == "__main__":
#     main()
