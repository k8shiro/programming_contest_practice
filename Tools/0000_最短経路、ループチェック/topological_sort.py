"""
非辞書順バージョン
トポロジカルソートとは：

各辺 (u → v) に対して、u が v よりも前に現れるようなノードの並び順を求めること。

つまり「依存関係を守るように並び替える」操作です。
"""

from collections import defaultdict, deque
from typing import Dict, List, Tuple, Any

def topological_sort(graph: Dict[Any, List[Any]]) -> List[Any]:
    """
    汎用的なトポロジカルソート関数（Kahn's Algorithm）

    Args:
        graph (dict): 隣接リスト形式の有向グラフ。
                      例: {'A': ['B'], 'B': ['C'], 'C': []}

    Returns:
        List[Any]: トポロジカル順序のノードリスト。
                   閉路がある場合は空リストを返す。
    """
    # すべてのノードを列挙（キーと値に出てくるノードを統合）
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors)

    # 入次数の辞書を初期化
    in_degree = {node: 0 for node in nodes}

    # 各ノードの入次数を計算
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # 入次数が0のノードをキューに入れる
    queue = deque([node for node in nodes if in_degree[node] == 0])

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # 隣接ノードの入次数を1つ減らす
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            # 入次数が0になったらキューに追加
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # トポロジカル順序に含まれるノード数が全体と一致しなければ閉路あり
    if len(result) != len(nodes):
        return []  # 閉路があるためトポロジカルソート不可

    return result



if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    print("Graph:", graph)

    order = topological_sort(graph)
    if order:
        print("Topological Sort:", order)
    else:
        print("Graph contains a cycle!")



    graph = {
        '1': [],
        '2': ['1', '4'],
        '3': ['4'],
        '4': []
    }
    print("Graph:", graph)

    order = topological_sort(graph)
    if order:
        print("Topological Sort:", order)
    else:
        print("Graph contains a cycle!")
