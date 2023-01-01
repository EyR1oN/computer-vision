def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    list_ = []
    while queue:
        m = queue.pop(0)
        list_.append(m)
        for neighbour in graph[m]:
          if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

    return list_
