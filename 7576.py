# 토마토

from collections import deque
n, m = map(int,input().split())

tomato = [list(map(int, input().split())) for _ in range(m)]

ripe = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0
# 익은 토마토 위치
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            ripe.append((i,j))
        elif tomato[i][j] == 0:
            cnt += 1
day = 0
while ripe and cnt:
    for _ in range(len(ripe)):
        x,y = ripe.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                cnt -= 1
                ripe.append((nx,ny))
    day += 1

if cnt == 0:
    print(day)
else:
    print(-1)