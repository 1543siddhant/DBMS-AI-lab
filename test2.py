graph={
      0:[1,2,3],
      1:[0],
      2:[3,0,4],
      3:[2,0],
      4:[2]
      }

def dfs(graph,start_N):
    visited[start_N] = 1
    print(start_N)
    for child in graph[start_N]:
        if not visited[child]:
            dfs(graph,child)
print("Depth first search")
visited = [0] * 5
dfs(graph,0)

def bfs(graph,start_N):
    queue = [start_N]
    visited = [start_N]
    while queue:
        curr = queue.pop(0)
        print(curr)
        for child in graph[curr]:
            if child not in visited:
                queue.append(child)
                visited.append(child)

print("Breadth first search")
bfs(graph,0)

def dfs(graph, visited, start_node):
    stack = [start_node]
    while stack:
        curr = stack.pop()
        if curr not in visited:
            print(curr)  
            visited.add(curr)
            for neighbour in reversed(graph[curr]):
                if neighbour not in visited:
                    stack.append(neighbour)
visited = set()
print("---------------------------------------------")
print("DFS Using stack")
dfs(graph,visited,0)
