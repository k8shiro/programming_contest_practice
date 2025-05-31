class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # 各要素の親
        self.rank = [0] * size           # ランク（木の深さ）
        self.size = [1] * size           # 各集合のサイズ（初期は1）

    def find(self, x):
        """
        x の親を見つける
        x が属する集合の代表元を返す
        """

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def union(self, x, y):
        """
        x と y を同じ集合に統合する
        x と y が同じ集合に属している場合は何もしない
        """

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        # 小さい方の木を大きい方に統合し、サイズも更新
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

    def connected(self, x, y):
        """
        x と y が同じ集合に属しているかを確認する
        """

        return self.find(x) == self.find(y)

    def group_size(self, x):
        """
        x が属する集合（連結成分）のサイズを返す
        """
        return self.size[self.find(x)]




def main():
    # 要素0〜9までの10個の集合を初期化（全て別々の集合）
    uf = UnionFind(10)

    # グループを統合していく
    uf.union(1, 2)  # 1と2を同じグループに
    uf.union(2, 3)  # 2と3も同じグループ → 1,2,3は同じ集合になる

    uf.union(4, 5)  # 4と5を同じグループに

    # グループのサイズを確認
    print(uf.group_size(1))  # 3（1,2,3がつながっている）
    print(uf.group_size(4))  # 2（4,5がつながっている）
    print(uf.group_size(0))  # 1（0はどこともつながっていない）

    # グループに属しているか確認
    print(uf.connected(1, 3))  # True（1,2,3はつながっている）
    print(uf.connected(1, 4))  # False（1と4は別の集合）

    # 統合してつながるようにする
    uf.union(3, 4)

    # 今度はつながっている
    print(uf.connected(1, 5))  # True（1-2-3-4-5が連結）

if __name__ == "__main__":
    main()