from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    N, S = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))

    SUBSET_SUM = [False] * (S + 1)
    SUBSET_SUM[0] = True

    for a in A:
        # 逆順にSから0までループ
        for idx in range(S, -1, -1):
            if SUBSET_SUM[idx] and idx + a <= S:
                SUBSET_SUM[idx + a] = True
    if SUBSET_SUM[S]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()