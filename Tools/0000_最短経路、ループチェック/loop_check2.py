
import networkx as nx

# 有向グラフのループチェック
# nx.is_directed_acyclic_graph
# Trueなら閉路なし
# Falseなら閉路あり
G = nx.DiGraph()
G.add_edges_from([(0, 1), (1, 2), (2, 0)])

has_cycle = not nx.is_directed_acyclic_graph(G)
print(has_cycle)  # True 


# 無向グラフのループチェック
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 0)])

has_cycle = not nx.is_forest(G)
print(has_cycle)  # True
