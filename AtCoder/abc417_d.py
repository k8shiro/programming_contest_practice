from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

from decimal import Decimal

# メモ化
from functools import lru_cache

# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18

# 10^9 + 7
MOD = 10**9 + 7


def main():
    N = int(stdin.readline().strip())

    presents = []
    for _ in range(N):
        P, A, B = map(int, stdin.readline().split())
        presents.append((P, A, B))

    Q = int(stdin.readline().strip())
    queries = []
    for i in range(Q):
        X = int(stdin.readline().strip())
        queries.append(X)

    MAX_T = max(p + a for p, a, b in presents)
    # dp[i][j] := i番目以降のプレゼントを受け取るときのテンションがjのときの、最終的なテンションの値
    dp = [[0] * (MAX_T + 1) for _ in range(N + 1)]
    for j in range(MAX_T + 1):
        dp[N][j] = j

    # 逆順でDPを計算
    for i in range(N - 1, -1, -1):
        p, a, b = presents[i]
        for j in range(MAX_T + 1):
            # 現在のテンションの値がプレゼントの価値以下なら +A, そうでなければ -B
            if j <= p:
                nj = j + a
                if nj > MAX_T:
                    nj = MAX_T
                dp[i][j] = dp[i + 1][nj]
            else:
                dp[i][j] = dp[i + 1][j - min(j, b)]


    import bisect
    from itertools import accumulate
    cumsum_B = list(accumulate(b for p, a, b in presents))

    for x in queries:
        if x <= MAX_T:
            print(dp[0][x])
            continue

        # 二分探索で何回減らせば範囲内に入るかを見つける
        target = x - MAX_T
        pos = bisect.bisect_left(cumsum_B, target)

        if pos == N:
            print(x - cumsum_B[-1])
            continue
        else:
            remaining_tension = x - cumsum_B[pos]
            if remaining_tension < 0:
                remaining_tension = 0
            print(dp[pos+1][remaining_tension])
            continue

if __name__ == "__main__":
    main()
