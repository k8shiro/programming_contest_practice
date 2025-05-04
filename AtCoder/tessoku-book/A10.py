from sys import stdin

def main():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    D = int(stdin.readline())

    # 左から見たときのAの最大値
    MAX_A_LEFT = [0] * (N + 2)
    tmp_max = -1
    for i in range(1 , N + 1):
        if A[i-1] > tmp_max:
            tmp_max = A[i-1]
        MAX_A_LEFT[i] = tmp_max
    # 右から見たときのAの最大値
    MAX_A_RIGHT = [0] * (N + 2)
    tmp_max = -1
    for i in range(N , 0, -1):
        if A[i-1] > tmp_max:
            tmp_max = A[i-1]
        MAX_A_RIGHT[i] = tmp_max

    # print(MAX_A_LEFT)
    # print(MAX_A_RIGHT)

    for _ in range(D):
        L, R = map(int, stdin.readline().split())
        L_MAX = MAX_A_LEFT[L-1]
        R_MAX = MAX_A_RIGHT[R + 1]
        ANS = max(L_MAX, R_MAX)
        print(ANS)


if __name__ == "__main__":
    main()