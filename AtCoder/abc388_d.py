from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


def main():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    imos = [0] * (N + 1)

    for adult_idx in range(N):
        # 先にimosの清算をする
        if adult_idx != 0:
            imos[adult_idx] += imos[adult_idx - 1]
            A[adult_idx] += imos[adult_idx]

        child_num = N - 1 - adult_idx
        present_num = min(child_num, A[adult_idx])
        if present_num > 0:
            imos[adult_idx + 1] += 1
            imos[adult_idx + 1 + present_num] -= 1
            A[adult_idx] -= present_num

    print(" ".join(map(str, A)))


if __name__ == "__main__":
    main()

# 単純探索TLE
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)


# def main():
#     N = int(stdin.readline())
#     A = list(map(int, stdin.readline().split()))

#     for idx in range(N):
#         for adult_idx in range(idx):
#             if A[adult_idx] == 0:
#                 continue
#             else:
#                 A[adult_idx] -= 1
#                 A[idx] += 1
#     print(" ".join(map(str, A)))

# if __name__ == "__main__":
#     main()
