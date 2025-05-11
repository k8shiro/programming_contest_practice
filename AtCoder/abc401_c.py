from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

mod = 10**9

from collections import deque
def main():
    N, K = map(int, stdin.readline().split())

    dq = deque()
    nums = [1 for _ in range(K)]
    dq.extend(nums)

    sum_i = sum(dq)
    for _ in range(N-K+1):
        dq.append(sum_i % mod)
        sum_i = (sum_i * 2 - dq.popleft()) % mod

    print(dq[-1] % mod)


if __name__ == "__main__":
    main()