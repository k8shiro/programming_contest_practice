from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)


# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18

A = []
def main():
    H, W = map(int, stdin.readline().split())
    global A
    for _ in range(H):
        A.append(list(map(int, stdin.readline().split())))

    # A全部のXORを求める
    total_xor = cal_total_xor(A)

    used = 'F' * H * W # 探索済みの記録
    ans = dfs(H, W, used, total_xor)
    print(ans)



def cal_total_xor(A):
    total_xor = 0
    for row in A:
        for value in row:
            if value < 0:
                continue
            total_xor ^= value
    return total_xor

from functools import lru_cache
@lru_cache(None)
def dfs(H, W, used, total_xor):
    return_total_xor = total_xor
    for h in range(H):
        for w in range(W):
            if w+1 < W and used[h * W + w] == 'F' and used[h * W + w + 1] == 'F':
                _total_xor = total_xor ^ A[h][w] ^ A[h][w+1]
                # A[h][w] = -1
                # A[h][w+1] = -1
                _used = used[:]
                idx = h * W + w
                _used = _used[:idx] + 'T' + _used[idx+1:]
                idx = h * W + w + 1
                _used = _used[:idx] + 'T' + _used[idx+1:]
                _total_xor = max(
                    _total_xor,
                    dfs(H, W, _used, _total_xor)
                )
                return_total_xor = max(return_total_xor, _total_xor)
            if h+1 < H and used[h * W + w] == 'F' and used[(h + 1) * W + w] == 'F':
                _total_xor = total_xor ^ A[h][w] ^ A[h+1][w]
                # A[h][w] = -1
                # A[h+1][w] = -1
                _used = used[:]
                idx = h * W + w
                _used = _used[:idx] + 'T' + _used[idx+1:]
                idx = (h + 1) * W + w
                _used = _used[:idx] + 'T' + _used[idx+1:]
                _total_xor = max(
                    _total_xor,
                    dfs(H, W, _used, _total_xor)
                )
                return_total_xor = max(return_total_xor, _total_xor)
    return return_total_xor

                



if __name__ == "__main__":
    main()