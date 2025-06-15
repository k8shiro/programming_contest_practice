def has_cycle_directed(graph, N):
    visited = [False] * N
    on_stack = [False] * N

    def dfs(v):
        visited[v] = True
        on_stack[v] = True
        for to in graph[v]:
            if not visited[to]:
                if dfs(to):
                    return True
            elif on_stack[to]:
                return True
        on_stack[v] = False
        return False

    for v in range(N):
        if not visited[v]:
            if dfs(v):
                return True
    return False

# グラフは0から始まること
graph = {
    0: [1],
    1: [2],
    2: [0],  # 0→1→2→0 というループ
    3: []
}
print(has_cycle_directed(graph, 4))  # True
