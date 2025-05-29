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
    N, M = map(int, stdin.readline().split())
    
    PATHS = [[] for _ in range(N + 1)]
    DIST = [INT_MAX] * (N + 1)
    DIST[1] = 0
    CNT = [0] * (N + 1)
    CNT[1] = 1
    

    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        PATHS[A].append(B)
        PATHS[B].append(A)

    from collections import deque
    queue = deque([1])
    while queue:
        city = queue.popleft()

        for next_city in PATHS[city]:
            if DIST[next_city] == INT_MAX:
                DIST[next_city] = DIST[city] + 1
                CNT[next_city] = CNT[city]
                queue.append(next_city)
            elif DIST[next_city] == DIST[city] + 1:
                CNT[next_city] += CNT[city]
                CNT[next_city] %= MOD

    print(CNT[N])


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
#     N, M = map(int, stdin.readline().split())
    
#     PATHS = [[False] * (N + 1) for _ in range(N + 1)]

#     for _ in range(M):
#         A, B = map(int, stdin.readline().split())
#         PATHS[A][B] = True
#         PATHS[B][A] = True

#     from collections import deque
#     queue = deque([(1, {1})])

#     for _ in range(N):
#         next_queue = deque()
#         count = 0
#         while queue:
#             city, visited = queue.popleft()
#             # print(f"現在の都市: {city}, 訪問済み: {visited}")

#             for next_city in range(1, N + 1):
#                 if PATHS[city][next_city] and next_city == N:
#                     count += 1
#                 elif PATHS[city][next_city] and next_city not in visited:
#                     new_visited = visited | {next_city}
#                     next_queue.append((next_city, new_visited))

#         if count != 0:
#             print(count)
#             return
#         queue = next_queue
#     print(0)




# if __name__ == "__main__":
#     main()