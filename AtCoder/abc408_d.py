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

    queries = []
    for _ in range(T):
        N = int(stdin.readline().strip())
        S = str(stdin.readline().strip())
        queries.append((N, S))

    for N, S in queries:
        sum_1 = [0] * (N + 1)
        for i in range(N):
            sum_1[i + 1] = sum_1[i] + (1 if S[i] == '1' else 0)
        total_1 = sum_1[N]
        min_ops = N

        min_ops = min(min_ops, total_1)
        min_ops = min(min_ops, N - total_1)

        for i in range(N + 1):
            ops1 = sum_1[i] + (N - i - (total_1 - sum_1[i]))
            min_ops = min(min_ops, ops1)
            ops2 = (i - sum_1[i]) + (total_1 - sum_1[i])
            min_ops = min(min_ops, ops2)

        min_left = [float('inf')] * (N + 1)
        for i in range(N + 1):
            val = 2 * sum_1[i] - i
            if i > 0:
                min_left[i] = min(min_left[i-1], val)
            else:
                min_left[i] = val

        for j in range(N + 1):
            cost = min_left[j] - 2 * sum_1[j] + j + total_1
            min_ops = min(min_ops, cost)

        print(min_ops)





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
#     T = int(stdin.readline().strip())

#     queries = []
#     for _ in range(T):
#         N = int(stdin.readline().strip())
#         S = str(stdin.readline().strip())
#         queries.append((N, S))

#     for N, S in queries:
#         sum_1 = [0] * (N + 1)
#         for i in range(N):
#             sum_1[i + 1] = sum_1[i] + (1 if S[i] == '1' else 0)

#         total_1 = sum_1[N]
#         min_ops = N

#         # すべて '0'
#         min_ops = min(min_ops, total_1)

#         # すべて '1'
#         min_ops = min(min_ops, N - total_1)

#         # 先頭 i 個が '0', 残り '1'
#         for i in range(N + 1):
#             ops = sum_1[i] + (N - i - (total_1 - sum_1[i]))
#             min_ops = min(min_ops, ops)

#         #  先頭 i 個が '1', 残り '0'
#         for i in range(N + 1):
#             ops = (i - sum_1[i]) + (total_1 - sum_1[i])
#             min_ops = min(min_ops, ops)

#         # 区間 [l, r) が '1', 残り '0'
#         for l in range(N + 1):
#             for r in range(l, N + 1):
#                 cost = (r - l) - (sum_1[r] - sum_1[l]) + (total_1 - (sum_1[r] - sum_1[l]))
#                 min_ops = min(min_ops, cost)

#         print(min_ops)





# if __name__ == "__main__":
#     main()


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
#     T = int(stdin.readline().strip())

#     queries = []
#     for _ in range(T):
#         N = int(stdin.readline().strip())
#         S = str(stdin.readline().strip())
#         queries.append((N, S))

#     for N, S in queries:
#         sum_1 = [0] * (N + 1)
#         for i in range(N):
#             sum_1[i + 1] = sum_1[i] + (1 if S[i] == '1' else 0)

#         total_1 = sum_1[N]
#         min_ops = N  # 最大でも全部ひっくり返す

#         for l in range(N + 1):
#             for r in range(l, N + 1):
#                 in_1 = sum_1[r] - sum_1[l]
#                 in_0 = (r - l) - in_1
#                 out_1 = total_1 - in_1
#                 ops = in_0 + out_1
#                 min_ops = min(min_ops, ops)

#         print(min_ops)





# if __name__ == "__main__":
#     main()


# WA
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
#     T = int(stdin.readline().strip())

#     queries = []
#     for _ in range(T):
#         N = int(stdin.readline().strip())
#         S = str(stdin.readline().strip())
#         queries.append((N, S))

#     for N, S in queries:
#         ans = count_op(S)
#         if ans == float('inf'):
#             ans = 0
#         print(ans)



# import re

# def count_op(s):
#     # 1の連続区間を見つける
#     part_1 = [(m.start(), m.end()) for m in re.finditer(r'1+', s)]
#     # rint(part_1)
    
#     total_1 = s.count('1')
#     total_0 = s.count('0')
#     min_ops = float('inf')

#     for start, end in part_1:
#         ones_to_zero = total_1 - (end - start)
#         zeros_to_one = s[:start].count('0') + s[end:].count('0')
#         min_ops = min(min_ops, ones_to_zero, zeros_to_one)

#     return min_ops





# if __name__ == "__main__":
#     main()



# WA
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
#     T = int(stdin.readline().strip())

#     queries = []
#     for _ in range(T):
#         N = int(stdin.readline().strip())
#         S = str(stdin.readline().strip())
#         queries.append((N, S))

#     for N, S in queries:
#         pre_s = 'x'
#         parts = []
#         for s in S:
#             if s == pre_s:
#                 parts[-1] += s
#             else:
#                 parts.append(s)
#                 pre_s = s
#         # print("============")
#         # print(parts)
#         if len(parts) == 1:
#             print(0)
#             continue
#         if parts[0][0] == '0':
#             parts = parts[1:]
#         if parts[-1][0] == '0':
#             parts = parts[:-1]
#         if len(parts) == 1:
#             print(0)
#             continue

#         count_0 = 0
#         max_0 = 0
#         count_1 = 0
#         max_1 = 0
#         for p in parts:
#             if p[0] == '0':
#                 count_0 += len(p)
#                 max_0 = max(max_0, len(p))
#             else:
#                 count_1 += len(p)
#                 max_1 = max(max_1, len(p))
        
#         print(count_0, max_0, count_1, max_1)
#         ans = min(count_0, count_1 - max_1)
#         print(ans)





# if __name__ == "__main__":
#     main()
