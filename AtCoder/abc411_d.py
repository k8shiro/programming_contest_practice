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


query_list = []
def main():
    global query_list
    N, Q = map(int, stdin.readline().strip().split())
    query_list = []
    for _ in range(Q):
        query = list(map(str, stdin.readline().strip().split()))
        query_list.append(query)

    ans = f(Q-1, 0)
    print(''.join(ans))

def f(t, p):
    global query_list
    query = query_list[t]
    # print(t, p, query)
    if t == -1:
        return []

    _p = int(query[1])
    if (query[0] == '1' and p != _p) or (query[0] == '2' and p != _p) or (query[0] == '3' and p != 0):
        return f(t-1, p)
    else:
        if query[0] == '1':
            return f(t-1, 0)
        elif query[0] == '2':
            s = query[2]
            tmp = f(t-1, _p)
            tmp.append(s)
            return tmp
        elif query[0] == '3':
            return f(t-1, _p)



 




if __name__ == "__main__":
    main()


# from sys import stdin

# def main():
#     N, Q = map(int, stdin.readline().strip().split())

#     pc_list = [[] for _ in range(N+1)] # 0がサーバー

#     for i in range(1, Q + 1):
#         query = list(map(str, stdin.readline().strip().split()))
#         if query[0] == '1':
#             p = int(query[1]) # 0-indexed
#             pc_list[p] = pc_list[0] # サーバーの内容をPCにコピー
#         elif query[0] == '2':
#             p = int(query[1])
#             s = query[2]
#             tmp = ''.join(pc_list[p])
#             tmp += s
#             pc_list[p] = [tmp]
#         elif query[0] == '3':
#             p = int(query[1])
#             pc_list[0] = pc_list[p] # PCの内容をサーバーにコピー

#     # サーバーの内容を出力
#     print(''.join(pc_list[0]))

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
#     N, Q = map(int, stdin.readline().strip().split())
#     query_list = []
#     for _ in range(Q):
#         query = list(map(str, stdin.readline().strip().split()))
#         query_list.append(query)

#     server = ""
#     pc_list = ["" for _ in range(N)]

#     for query in query_list:
#         if query[0] == '1':
#             p = int(query[1]) - 1 # 0-indexed
#             pc_list[p] = server
#         elif query[0] == '2':
#             p = int(query[1]) - 1 # 0-indexed
#             s = query[2]
#             pc_list[p] += s
#         elif query[0] == '3':
#             p = int(query[1]) - 1
#             server = pc_list[p]

#     # print(query_list)
#     # print(pc_list)
#     print(server)




# if __name__ == "__main__":
#     main()
