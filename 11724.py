
def is_connected(idx,depth):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            is_connected(i,depth+1)



# 정점의 개수n, 간선의 개수 m
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    # 연결 된 정점 x,y
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
cnt = 0

for i in range(1,n+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = True
        else:
            is_connected(i,0)
            cnt += 1
print(cnt)