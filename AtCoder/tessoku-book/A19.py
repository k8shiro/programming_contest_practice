from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    N, W = map(int, stdin.readline().split())

    dp = [-1] * (W + 1)
    dp[0] = 0
    for _ in range(N):
        w, v = map(int, stdin.readline().split())

        for idx in range(W, -1, -1):
            if dp[idx] != -1 and idx + w <= W:
                dp[idx + w] = max(dp[idx] + v, dp[idx + w])
    ANS = max(dp)
    print(ANS)
    

if __name__ == "__main__":
    main()