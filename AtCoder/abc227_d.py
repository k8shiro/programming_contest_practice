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
    N, K, = map(int, stdin.readline().strip().split())
    A = list(map(int, stdin.readline().strip().split()))

    # ∑min(x,Ai)≥Kx 
    left = 0
    right = 2 * (10 ** 18)+1

    while left < right:
        x = (left + right + 1) // 2
        if is_ok(A, K, x):
            left = x
        else:
            right = x - 1
    print(left)


    
def is_ok(A, K, x):
    total = 0
    for a in A:
        total += min(a, x)
    return total >= K * x




if __name__ == "__main__":
    main()





# def main():
#     N, K, = map(int, stdin.readline().strip().split())
#     A = list(map(int, stdin.readline().strip().split()))

#     from sortedcontainers import SortedList
#     A = SortedList(A)  # ソート済みで保持

#     count = 0
#     while len(A) >= K:
#         new_a = []
#         for _ in range(K):
#             a = A.pop()  # 最大値をK個取り出す（末尾）
#             new_a.append(a)
        
#         count += 1

#         for a in new_a:
#             a -= 1
#             if a > 0:
#                 A.add(a)  # O(log N) で挿入

#     print(count)




# if __name__ == "__main__":
#     main()


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
#     N, K, = map(int, stdin.readline().strip().split())
#     A = list(map(int, stdin.readline().strip().split()))

#     A.sort()
    
#     import bisect
#     count = 0
#     while len(A) >= K:
#         new_a = []
#         for _ in range(K):
#             a = A.pop()
#             new_a.append(a)
        
#         count += 1

#         for a in new_a:
#             a -= 1
#             if a > 0:
#                 bisect.insort(A, a)

#     print(count)





# if __name__ == "__main__":
#     main()
