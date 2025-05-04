from sys import stdin

def main():
    N, X = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))

    idx_left = 0
    idx_right = N - 1
    while True:
        idx = (idx_left + idx_right) // 2
        if A[idx] == X:
            print(idx + 1)
            return
        elif A[idx] < X:
            idx_left = idx + 1
        else:
            idx_right = idx - 1



if __name__ == "__main__":
    main()