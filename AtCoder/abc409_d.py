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
    for _ in range(T):
        N = int(stdin.readline().strip())
        S = list(str(stdin.readline().strip()))
        if len(S) == 1:
            print(''.join(S))
            continue

        solve(S, N)

def solve(S, N):
    for idx in range(1, N):
        if S[idx-1] > S[idx]:
            while True:
                OLD_S = ''.join(S)
                S[idx-1], S[idx] = S[idx], S[idx-1]
                NEW_S = ''.join(S)
                # print(OLD_S, NEW_S)
                if OLD_S < NEW_S:
                    print(OLD_S)
                    return
                idx += 1
                if idx >= N:
                    print(''.join(S))
                    return

    print(''.join(S))
    return


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
#     for _ in range(T):
#         N = int(stdin.readline().strip())
#         S = str(stdin.readline().strip())
#         min_s = S

#         for l in range(N):
#             for r in range(l, N):
#                 rotated = (
#                     S[:l] +      
#                     S[l+1:r+1] + 
#                     S[l] +       
#                     S[r+1:]      
#                 )
#                 if rotated < min_s:
#                     min_s = rotated

#         print(min_s)




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
#     for _ in range(T):
#         N = int(stdin.readline().strip())
#         S = list(str(stdin.readline().strip()))
#         if len(S) == 1:
#             print(''.join(S))
#             continue

#         flag = True
#         for idx in range(1, N):
#             if S[idx-1] > S[idx]:
#                 while S[idx-1] > S[idx]:
#                     tmp = S[idx-1]
#                     S[idx-1] = S[idx]
#                     S[idx] = tmp
#                     idx += 1
#                     if idx >= N:
#                         break
#                 break
#         print(''.join(S))




# if __name__ == "__main__":
#     main()