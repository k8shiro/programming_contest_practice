"""
ある頂点から他のすべての頂点への最短距離を求めるダイクストラ法

"""

import heapq  # 優先度付きキュー（最小ヒープ）を使うための標準モジュール

def dijkstra(graph, start):
    """
    ダイクストラ法を使って、スタートノードから他のすべてのノードへの
    最短距離を求める関数。

    :param graph: 各ノードとその隣接ノード・重みを辞書形式で表したグラフ
                  例: {'A': [('B', 2), ('C', 5)], 'B': [('C', 1)]}
    :param start: 探索を開始するノード（例: 'A'）
    :return: 各ノードへの最短距離を格納した辞書
    """

    # 各ノードへの最短距離を記録する辞書（初期値はすべて無限大）
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # スタートノードへの距離は 0

    # 探索キュー（(距離, ノード) のタプル）を優先度付きキューとして使う
    queue = [(0, start)]  # 初期状態としてスタートノードを追加

    # キューが空になるまでループ
    while queue:
        # ノードを取り出す
        current_distance, current_node = heapq.heappop(queue)

        # 既に発見済みのより短い距離があればスキップ
        if current_distance > distances[current_node]:
            continue

        # 現在のノードに隣接するノードを調べる
        for neighbor, weight in graph[current_node]:
            # 現在の距離 + このエッジの重み を仮の距離とする
            distance = current_distance + weight

            # より短い距離が見つかった場合は更新
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # キューに追加（まだ探索していないが、今後取り出すため）
                heapq.heappush(queue, (distance, neighbor))

    # 最終的な距離マップを返す
    return distances


def main():
    # ノードごとに「隣接ノードと重み」のリストを持つ辞書形式
    graph = {
        'A': [('B', 2), ('C', 5)],
        'B': [('C', 1), ('D', 3)],
        'C': [('D', 2)],
        'D': []
    }

    result = dijkstra(graph, 'A')

    # 各ノードへの最短距離を表示
    for node, distance in result.items():
        print(f"距離 A → {node} = {distance}")

if __name__ == "__main__":
    main()