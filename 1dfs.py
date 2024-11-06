
def dfs(Graph,visited,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in Graph[node]:
            dfs(Graph,visited,neighbour)
            
            

def bfs(Graph,visited,node):
    visited.add(node)
    queue=[]
    queue.append(node)
    while queue:
        node=queue.pop(0)
        print(node)
        for neighbour in Graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                

Graph={
      0:[1,2,3],
      1:[0],
      2:[3,0,4],
      3:[2,0],
      4:[2]
      }

visited=set()
print("This is for DFS ")
dfs(Graph,visited,0)
visited.clear()
print("This is for BFS")
bfs(Graph,visited,0)


def dfs(graph, visited, start_node):
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)  
            visited.add(node)
            for neighbour in reversed(Graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

dfs(graph,visited,0)
