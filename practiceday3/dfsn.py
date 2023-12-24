def DFS(graph, start, visited=None):
    if visited == None:
        visited = set()
    visited.add(start)
    print(start)
    for i in graph[start]:
        if i not in visited:
            visited.add(i)
            DFS(graph, i, visited)
graph = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B", "D", "E"],
    "D": ["A", "C", "E"],
    "E": ["C", "D"]
}
# BFS(graph, "A")
DFS(graph, "C")