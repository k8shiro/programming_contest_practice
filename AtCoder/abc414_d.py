from sys import stdin

def main():
    import sys
    sys.setrecursionlimit(10**6)

    N, M = map(int, stdin.readline().strip().split())
    X = list(map(int, stdin.readline().strip().split()))
    
    if M >= N:
        print(0)
        return

    X.sort()
    gaps = []

    for i in range(N - 1):
        gaps.append(X[i + 1] - X[i])

    gaps.sort(reverse=True)

    print(sum(gaps[M - 1:]))

if __name__ == "__main__":
    main()


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
#     N, M = map(int, stdin.readline().strip().split())
#     X = list(map(int, stdin.readline().strip().split()))

#     X = set(X)
#     X = sorted(X)
#     min_x = X[0]
#     X = [x - min_x for x in X]
#     #print(X)
#     if len(X) < M:
#         print(0)
#         return

#     splits = split_array(X, M)
#     ans = INT_MAX
#     for split in splits:
#         denpa = 0
#         for s in split:
#             denpa += s[-1] - s[0]
#         ans = min(ans, denpa)
#     print(ans)
    
# def split_array(arr, k):
#     return _split_array(arr, 0, k)

# def _split_array(arr, start, k):
#     result = []

#     if k == 1:
#         if start < len(arr):
#             result.append([arr[start:]])
#         return result

#     # endは start+1 から len(arr) - (k - 1) まで
#     for end in range(start + 1, len(arr) - k + 2):
#         first = arr[start:end]
#         rest_splits = _split_array(arr, end, k - 1)

#         for rest in rest_splits:
#             result.append([first] + rest)

#     return result

# if __name__ == "__main__":
#     main()
