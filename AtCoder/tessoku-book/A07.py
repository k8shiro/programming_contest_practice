from sys import stdin

def main():
    D = int(stdin.readline())
    N = int(stdin.readline())

    COUNT_LIST = [0] * (D+1) # その日の増減を表す

    for _ in range(N):
        L, R = map(int, stdin.readline().split())
        COUNT_LIST[L-1] += 1
        COUNT_LIST[R] -= 1

    COUNT = 0
    for c in COUNT_LIST[:-1]:
        COUNT += c
        print(COUNT)
    return


if __name__ == "__main__":
    main()

