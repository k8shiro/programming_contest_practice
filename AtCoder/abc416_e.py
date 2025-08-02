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


from sys import stdin

def main():
    N, M = map(int, stdin.readline().split())
    

    INF = 10**18
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    

    for i in range(1, N + 1):
        dist[i][i] = 0
    

    for _ in range(M):
        A, B, C = map(int, stdin.readline().split())
        dist[A][B] = min(dist[A][B], C)
        dist[B][A] = min(dist[B][A], C)
    

    K, T = map(int, stdin.readline().split())
    airports = []
    if K > 0:
        D = list(map(int, stdin.readline().split()))
        airports = D[:]

        for i in range(K):
            for j in range(i + 1, K):
                dist[D[i]][D[j]] = min(dist[D[i]][D[j]], T)
                dist[D[j]][D[i]] = min(dist[D[j]][D[i]], T)
    

    def floyd_warshall():
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                if dist[i][k] == INF:
                    continue
                for j in range(1, N + 1):
                    if dist[k][j] == INF:
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    floyd_warshall()
    
    Q = int(stdin.readline().strip())
    
    for _ in range(Q):
        query = list(map(int, stdin.readline().split()))
        
        if query[0] == 1:  # 新しい道路を追加
            x, y, t = query[1], query[2], query[3]
            if dist[x][y] > t:
                dist[x][y] = t
                dist[y][x] = t

                for i in range(1, N + 1):
                    for j in range(1, N + 1):
                        if dist[i][x] != INF and dist[y][j] != INF:
                            dist[i][j] = min(dist[i][j], dist[i][x] + t + dist[y][j])
                        if dist[i][y] != INF and dist[x][j] != INF:
                            dist[i][j] = min(dist[i][j], dist[i][y] + t + dist[x][j])
        
        elif query[0] == 2:  # 新しい空港を追加
            x = query[1]

            for airport in airports:
                if dist[x][airport] > T:
                    dist[x][airport] = T
                    dist[airport][x] = T
            airports.append(x)

            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if dist[i][x] != INF and dist[x][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][x] + dist[x][j])
        
        elif query[0] == 3:  # 全ペア最短距離の合計を計算
            total = 0
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    if i != j and dist[i][j] != INF:
                        total += dist[i][j]
            print(total)

if __name__ == "__main__":
    main()