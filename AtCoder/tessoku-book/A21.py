from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

def main():
    N = int(stdin.readline())
    PA = []
    lr_cost = [[-1] * N for _ in range(N)]
    for _ in range(N):
        p, a = map(int, stdin.readline().split())
        PA.append((p-1, a)) # 0-indexedに変換

    ans = dp(0, N - 1, PA, lr_cost)
    print(ans)
    


def dp(l, r, PA, lr_cost):
    if lr_cost[l][r] != -1:
        return lr_cost[l][r]


    if l == r:
        lr_cost[l][r] = 0
        return 0
    
    ans_l = dp(l + 1, r, PA, lr_cost) 
    if l + 1 <= PA[l][0] and PA[l][0] <= r:
        ans_l += PA[l][1]

    ans_r = dp(l, r - 1, PA, lr_cost)
    if l <= PA[r][0] and PA[r][0] <= r - 1:
        ans_r += PA[r][1]
    
    lr_cost[l][r] = max(ans_l, ans_r)
    return lr_cost[l][r]

if __name__ == "__main__":
    main()