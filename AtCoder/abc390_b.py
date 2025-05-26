from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))

    for idx in range(N):
        if idx == 0:
            continue
        if idx == 1:
            continue
        if A[idx] * A[idx - 2] != A[idx - 1] * A[idx - 1]:
            print("No")
            return
    print("Yes")





    

if __name__ == "__main__":
    main()