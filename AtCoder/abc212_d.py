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
    Q = int(stdin.readline().strip())
    


    queries = []
    for turn in range(Q):
        query = list(map(int, stdin.readline().split()))
        if query[0] == 1:
            x = query[1]
            queries.append((x, 1))
        if query[0] == 2:
            x = query[1]
            queries.append((x, 2))
        if query[0] == 3:
            queries.append((-1, 3))

    #print(queries)
    plus = 0
    for idx in reversed(range(len(queries))):
        if queries[idx][1] == 1:
            queries[idx] = (queries[idx][0] + plus, 1)
        if queries[idx][1] == 2:
            plus += queries[idx][0]
        if queries[idx][1] == 3:
            queries[idx] = (plus, 3)

    # bisectではTLEなのでSortedListを使う
    # from bisect import insort
    # sorted_list = []
    # for query in queries:
    #     if query[1] == 1:
    #         insort(sorted_list, query[0])
    #     if query[1] == 2:
    #         continue
    #     if query[1] == 3:
    #         plus = query[0]
    #         x = sorted_list.pop(0)
    #         print(x - plus)
    from sortedcontainers import SortedList

    sorted_list = SortedList()

    for query in queries:
        if query[1] == 1:
            sorted_list.add(query[0])  # O(log N)
        elif query[1] == 2:
            continue
        elif query[1] == 3:
            plus = query[0]
            x = sorted_list.pop(0)  # O(log N)
            print(x - plus)

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
#     Q = int(stdin.readline().strip())
    
#     import bisect
#     sorted_list = []

#     ans = 0
#     for _ in range(Q):
#         queries = list(map(int, stdin.readline().split()))
#         if queries[0] == 1:
#             x = queries[1]
#             bisect.insort(sorted_list, x)
#         if queries[0] == 2:
#             x = queries[1]
#             for idx in range(len(sorted_list)):
#                 sorted_list[idx] += x
#         if queries[0] == 3:
#             x = sorted_list.pop(0)
#             print(x)
        



# if __name__ == "__main__":
#     main()