from sys import stdin

def main():
    N, K = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))

    ANS = 0
    for i in range(N - 1):
        idx_l = i
        idx_r = N - 1

        while True:
            idx_m = (idx_l + idx_r) // 2
            if A[idx_m] - A[i] <= K:
                idx_l = idx_m + 1
            else:
                idx_r = idx_m - 1

            if idx_l > idx_r:
                break

        #print(A[i], A[idx_l - 1])
        ANS += idx_l - i - 1

    print(ANS)



if __name__ == "__main__":
    main()