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
    T = int(stdin.readline().strip())
    cases = []
    for _ in range(T):
        N, M = map(int, stdin.readline().split())
        A = list(map(int, stdin.readline().split()))
        B = list(map(int, stdin.readline().split()))
        cases.append((N, M, A, B))

    from sortedcontainers import SortedList
    for N, M, A, B in cases:
        A = [a % M for a in A]
        B = [b % M for b in B]

        A.sort()
        B.sort()
        sl = SortedList(A)

        total = 0
        for b in reversed(B):
            target = M - b
            idx = sl.bisect_left(target)
            if idx < len(sl):
                a = sl.pop(idx)
            else:
                a = sl.pop(0)
            total += (a + b) % M
        print(total)


if __name__ == "__main__":
    main()

# def main():
#     T = int(stdin.readline().strip())
#     cases = []
#     for _ in range(T):
#         N, M = map(int, stdin.readline().split())
#         A = list(map(int, stdin.readline().split()))
#         B = list(map(int, stdin.readline().split()))
#         cases.append((N, M, A, B))

#     for N, M, A, B in cases:
#         A = [a % M for a in A]
#         B = [b % M for b in B]

#         from collections import defaultdict
#         count_a = defaultdict(int)
#         for a in A:
#             count_a[a] += 1
        
#         total = 0
        
#         for b in B:
#             best_val = M
#             best_a = -1
            
#             for a in count_a:
#                 if count_a[a] > 0:
#                     val = (a + b) % M
#                     if val < best_val:
#                         best_val = val
#                         best_a = a
            
#             # 最適なaを1つ消費
#             count_a[best_a] -= 1
#             total += best_val
        
#         print(total)








# if __name__ == "__main__":
#     main()
