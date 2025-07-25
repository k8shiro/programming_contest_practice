class TreeManager:
    def __init__(self, n):
        """
        n: 節点の数（0 から n-1 まで）
        """
        self.n = n
        self.parent = [i for i in range(n)]  # 直接の親
        self.root = [i for i in range(n)]    # Union-Find用の代表親（根）
        self.children = [[] for _ in range(n)]  # 子ノードリスト

    def find_root(self, x):
        """
        xの先頭の親（木の根）を返す（Union-Find）
        経路圧縮を行う。
        """
        if self.root[x] != x:
            self.root[x] = self.find_root(self.root[x])
        return self.root[x]

    def connect(self, parent, child):
        """
        parentの下にchildを接続する。
        すでにどちらかが木に属していても統合する。
        """
        # すでに接続されているなら無視
        if self.parent[child] == parent:
            return

        # 子を持つ場合も含めて構造をつなげる
        self.parent[child] = parent
        self.children[parent].append(child)

        # Union-Find的な木の根を更新（childの根全体をparentの根にする）
        root_parent = self.find_root(parent)
        root_child = self.find_root(child)

        if root_parent != root_child:
            self.root[root_child] = root_parent

    def disconnect(self, parent, child):
        """
        parentとchildの接続を切断する。
        """
        if self.parent[child] != parent:
            return  # 接続されていないなら何もしない

        # 接続解除
        self.parent[child] = child  # 自分自身を親にする（孤立化）
        if child in self.children[parent]:
            self.children[parent].remove(child)

        # Union-Findの木の根を更新（切断された側を独立させる）
        def update_root(x, new_root):
            self.root[x] = new_root
            for ch in self.children[x]:
                update_root(ch, new_root)

        update_root(child, child)

    def get_direct_parent(self, x):
        """
        直接の親を返す。自身が根ならNoneを返す。
        """
        return None if self.parent[x] == x else self.parent[x]

    def get_children(self, x):
        """
        直接の子のリストを返す。子がない場合は空リストを返す。
        """
        return self.children[x]

    def get_root(self, x):
        """
        木の根（先頭の親）を返す。
        """
        return self.find_root(x)

    def get_all_descendants(self, x):
        """
        xの全ての子孫ノード（再帰）を返す。
        """
        result = []

        def dfs(v):
            for ch in self.children[v]:
                result.append(ch)
                dfs(ch)

        dfs(x)
        return result

    def is_connected(self, x, y):
        """
        xとyが同じ木に属しているか（根が同じか）を返す。
        """
        return self.find_root(x) == self.find_root(y)


def main():
    tm = TreeManager(10)

    tm.connect(0, 1)
    tm.connect(0, 2)
    tm.connect(1, 3)
    tm.connect(1, 4)

    print("root of 4:", tm.get_root(4))  # 0
    print("direct parent of 4:", tm.get_direct_parent(4))  # 1
    print("children of 1:", tm.get_children(1))  # [3, 4]
    print("descendants of 0:", tm.get_all_descendants(0))  # [1, 3, 4, 2]

    tm.disconnect(1, 4)

    print("After disconnecting 1 and 4:")
    print("root of 4:", tm.get_root(4))  # 4（独立）
    print("is_connected 0 and 4:", tm.is_connected(0, 4))  # False

if __name__ == "__main__":
    main()