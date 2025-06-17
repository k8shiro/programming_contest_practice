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
    N, Q = map(int, stdin.readline().strip().split())
    query_list = []
    for _ in range(Q):
        query = list(map(int, stdin.readline().strip().split()))
        query_list.append(query)
    nodes = dict()
    for i in range(1, N + 1):
        nodes[i] = {
            'parent': None,  # 直接の親
            'child': None,  # 子ノードリスト
        }


    for query in query_list:
        if query[0] == 1:
            # 1 x y: xの下にyを接続
            x, y = query[1], query[2]
            nodes[y]['parent'] = x
            nodes[x]['child'] = y

        elif query[0] == 2:
            # 2 x y: xとyの接続を切断
            x, y = query[1], query[2]
            nodes[y]['parent'] = None
            nodes[x]['child'] = None

        elif query[0] == 3:
            # 3 x: xの直接の親を出力
            x = query[1]

            ANS = []
            node = x
            while True:
                parent = nodes[node]['parent']
                if parent is None:
                    break
                ANS.append(parent)
                node = parent
            ANS.reverse()  # 逆順にして出力
            
            ANS.append(x)  # 自分自身も追加
            
            node = x
            while True:
                child = nodes[node]['child']
                if child is None:
                    break
                ANS.append(child)
                node = child

            print(len(ANS), *ANS)

 



if __name__ == "__main__":
    main()


# TLE
# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# from decimal import Decimal

# # メモ化
# from functools import lru_cache

# # 探索失敗用にINT_MAXを定義
# INT_MAX = 10**18

# # 10^9 + 7
# MOD = 10**9 + 7


# def main():
#     N, Q = map(int, stdin.readline().strip().split())
#     tm = TreeManager(N)
#     query_list = []
#     for _ in range(Q):
#         query = list(map(int, stdin.readline().strip().split()))
#         query_list.append(query)
#     # print("==============")
#     for query in query_list:
#         if query[0] == 1:
#             # 1 x y: xの下にyを接続
#             x, y = query[1] - 1, query[2] - 1
#             tm.connect(x, y)
#         elif query[0] == 2:
#             # 2 x y: xとyの接続を切断
#             x, y = query[1] - 1, query[2] - 1
#             tm.disconnect(x, y)
#         elif query[0] == 3:
#             # 3 x: xの直接の親を出力
#             x = query[1] - 1
#             node = tm.get_root(x)
#             ANS = []
#             while True:
#                 ANS.append(node + 1)  # 1-indexedで出力
#                 children = tm.get_children(node)
#                 if not children:
#                     break
#                 node = children[0]
#             print(len(ANS), *ANS)


            



# class TreeManager:
#     def __init__(self, n):
#         """
#         n: 節点の数（0 から n-1 まで）
#         """
#         self.n = n
#         self.parent = [i for i in range(n)]  # 直接の親
#         self.root = [i for i in range(n)]    # Union-Find用の代表親（根）
#         self.children = [[] for _ in range(n)]  # 子ノードリスト

#     def find_root(self, x):
#         """
#         xの先頭の親（木の根）を返す（Union-Find）
#         経路圧縮を行う。
#         """
#         if self.root[x] != x:
#             self.root[x] = self.find_root(self.root[x])
#         return self.root[x]

#     def connect(self, parent, child):
#         """
#         parentの下にchildを接続する。
#         すでにどちらかが木に属していても統合する。
#         """
#         # すでに接続されているなら無視
#         if self.parent[child] == parent:
#             return

#         # 子を持つ場合も含めて構造をつなげる
#         self.parent[child] = parent
#         self.children[parent].append(child)

#         # Union-Find的な木の根を更新（childの根全体をparentの根にする）
#         root_parent = self.find_root(parent)
#         root_child = self.find_root(child)

#         if root_parent != root_child:
#             self.root[root_child] = root_parent

#     def disconnect(self, parent, child):
#         """
#         parentとchildの接続を切断する。
#         """
#         if self.parent[child] != parent:
#             return  # 接続されていないなら何もしない

#         # 接続解除
#         self.parent[child] = child  # 自分自身を親にする（孤立化）
#         if child in self.children[parent]:
#             self.children[parent].remove(child)

#         # Union-Findの木の根を更新（切断された側を独立させる）
#         def update_root(x, new_root):
#             self.root[x] = new_root
#             for ch in self.children[x]:
#                 update_root(ch, new_root)

#         update_root(child, child)

#     def get_direct_parent(self, x):
#         """
#         直接の親を返す。自身が根ならNoneを返す。
#         """
#         return None if self.parent[x] == x else self.parent[x]

#     def get_children(self, x):
#         """
#         直接の子のリストを返す。
#         """
#         return self.children[x]

#     def get_root(self, x):
#         """
#         木の根（先頭の親）を返す。
#         """
#         return self.find_root(x)

#     def get_all_descendants(self, x):
#         """
#         xの全ての子孫ノード（再帰）を返す。
#         """
#         result = []

#         def dfs(v):
#             for ch in self.children[v]:
#                 result.append(ch)
#                 dfs(ch)

#         dfs(x)
#         return result

#     def is_connected(self, x, y):
#         """
#         xとyが同じ木に属しているか（根が同じか）を返す。
#         """
#         return self.find_root(x) == self.find_root(y)



# if __name__ == "__main__":
#     main()
