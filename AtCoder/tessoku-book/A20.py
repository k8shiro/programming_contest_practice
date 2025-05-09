from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    S = input()
    T = input()

    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]
    for s_i in range(len(S)):
        s = S[s_i]
        s_i += 1
        for t_i in range(len(T)):
            t = T[t_i]
            t_i += 1
            if s == t:
                dp[s_i][t_i] = dp[s_i - 1][t_i - 1] + 1
            else:
                dp[s_i][t_i] = max(dp[s_i - 1][t_i], dp[s_i][t_i - 1])
    print(dp[-1][-1])

            

    

if __name__ == "__main__":
    main()