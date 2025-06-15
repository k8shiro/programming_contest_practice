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

edges = {}
def main():
    global edges
    M = int(stdin.readline().strip())

    edges = {i: [] for i in range(9)}
    for _ in range(M):
        u, v = map(int, stdin.readline().strip().split())
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)

    P = list(map(int, stdin.readline().strip().split()))
    nodes = {i: -1 for i in range(9)}
    for key, val in enumerate(P):
        nodes[val-1] = key

    #print(nodes)
    (n1, n2, n3, n4, n5, n6, n7, n8, n9) = nodes.values()
    #print(n1, n2, n3, n4, n5, n6, n7, n8, n9)
    empty = 0
    for idx in range(9):
        if nodes[idx] == -1:
            empty = idx 
    res = solve(n1, n2, n3, n4, n5, n6, n7, n8, n9)
    print(res)


def solve(n1, n2, n3, n4, n5, n6, n7, n8, n9):
    from collections import deque

    idx = -1
    for i in range(9):
        if (n1, n2, n3, n4, n5, n6, n7, n8, n9)[i] == -1:
            idx = i
            break

    queue = deque()
    queue.append(((n1, n2, n3, n4, n5, n6, n7, n8, n9), idx))
    solved = set()
    solved.add((n1, n2, n3, n4, n5, n6, n7, n8, n9))
    count = 0
    while True:
        next_queue = deque()
        while queue:
            (n1, n2, n3, n4, n5, n6, n7, n8, n9), empty = queue.popleft()
            if (n1, n2, n3, n4, n5, n6, n7, n8, n9) == (0, 1, 2, 3, 4, 5, 6, 7, -1):
                return count
            for next_node in edges[empty]:
                new_nodes = list((n1, n2, n3, n4, n5, n6, n7, n8, n9))
                new_nodes[empty], new_nodes[next_node] = new_nodes[next_node], -1
                new_nodes = tuple(new_nodes)

                if new_nodes in solved:
                    continue

                next_queue.append((new_nodes, next_node))
                solved.add(new_nodes)
        queue = next_queue
        count += 1
        if not queue:
            break
    return -1



if __name__ == "__main__":
    main()
