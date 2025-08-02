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
    N, K, X = map(int, stdin.readline().split())
    S_list = []
    for i in range(N):
        S = str(stdin.readline().strip())
        S_list.append(S)
    
    results = []
    for i in range(N ** K):
        digits = to_base_n_digits_padded(i, N, K)
        concatenated = ""
        for d in digits:
            concatenated += S_list[d]
        
        results.append(concatenated)
    results.sort()
    print(results[X-1])

def to_base_n_digits_padded(X, N, K):
    if X == 0:
        digits = [0]
    else:
        digits = []
        while X > 0:
            digits.append(X % N)
            X //= N
        digits.reverse()
    
    padding = [0] * max(0, K - len(digits))
    return padding + digits

if __name__ == "__main__":
    main()


# def main():
#     N, K, X = map(int, stdin.readline().split())
#     S_list = []
#     for i in range(N):
#         S = str(stdin.readline().strip())
#         S_list.append(S)

#     S_list.sort()

#     digits = to_base_n_digits_padded(X-1, N, K)
#     #print(digits)

#     ans = []
#     for d in digits:
#         ans.append(S_list[d])

#     print(''.join(ans))



# def to_base_n_digits_padded(X, N, K):
#     if X == 0:
#         digits = [0]
#     else:
#         digits = []
#         while X > 0:
#             digits.append(X % N)
#             X //= N
#         digits.reverse()
    
#     padding = [0] * max(0, K - len(digits))
#     return padding + digits




# if __name__ == "__main__":
#     main()
