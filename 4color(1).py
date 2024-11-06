
def is_safe(graph, color, vertex, c):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c: 
            return False
    return True

def graph_coloring_util(graph, m, color, vertex):
    if vertex == len(graph): 
        return True
    
    rgb = ["Red","Green","Blue"]
    for c in rgb:
        if is_safe(graph, color, vertex, c):   
            color[vertex] = c 
            if graph_coloring_util(graph, m, color, vertex + 1):  
                return True
            color[vertex] = 0 

    return False


def graph_coloring(graph, m):
    n = len(graph)  
    color = [0] * n 
    
   
    if  graph_coloring_util(graph, m, color, 0):
        print("Solution exists. Assigned colors are:")
        for i in range(n):
             print(f"Vertex {i} ---> Color {color[i]}")
             
        return True
       
    print("Solution does not exist")
    return False


graph = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 0]
    ]
    
m = 3  
graph_coloring(graph, m)
