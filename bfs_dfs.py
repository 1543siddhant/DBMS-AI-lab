g={
    0:[1,2],
    1:[3,4,5],
    2:[0,3],
    3:[1,4],
    4:[5,3,1],
    5:[1,4]

}
vis =[]
def dfs(g,s):
    vis[s] = 1
    print(s)
    for c in g(s):
        if not vis[c]:
            dfs(g,c)

vis[0] * 9
dfs(g,0)