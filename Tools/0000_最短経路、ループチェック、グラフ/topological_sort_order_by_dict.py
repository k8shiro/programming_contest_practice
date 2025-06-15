"""
辞書順最小のトポロジカルソート
トポロジカルソートとは：

各辺 (u → v) に対して、u が v よりも前に現れるようなノードの並び順を求めること。

つまり「依存関係を守るように並び替える」操作です。
"""

import heapq
from typing import Dict, List, Any

def lex_smallest_toposort(graph: Dict[Any, List[Any]]) -> List[Any]:
    """
    辞書順最小のトポロジカル順序を1つ返す（閉路があると空リスト）

    Args:
        graph (dict): 隣接リスト形式の有向グラフ

    Returns:
        List[Any]: 辞書順最小のトポロジカル順序 or []（閉路あり）
    """

    # すべてのノードを抽出
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors)

    # 入次数の初期化
    in_degree = {node: 0 for node in nodes}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # 入次数0のノードをmin-heapに追加
    heap = [node for node in nodes if in_degree[node] == 0]
    heapq.heapify(heap)

    result = []

    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    # 閉路がある場合
    if len(result) != len(nodes):
        return []

    return result


if __name__ == "__main__":
    graph = {
        'A': ['C'],
        'B': ['C'],
        'C': ['D'],
        'D': []
    }
    print("Graph:", graph)

    order = lex_smallest_toposort(graph)
    if order:
        print("Lex smallest topological order:", order)
    else:
        print("Graph contains a cycle!")


    graph = {
        '1': [],
        '2': ['1', '4'],
        '3': ['4'],
        '4': []
    }
    print("Graph:", graph)

    order = lex_smallest_toposort(graph)
    if order:
        print("Lex smallest topological order:", order)
    else:
        print("Graph contains a cycle!")
