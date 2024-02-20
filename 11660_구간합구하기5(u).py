import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

preSum = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        preSum[i][j] = preSum[i][j-1] + preSum[i-1][j] - preSum[i-1][j-1] + arr[i-1][j-1]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    answer = preSum[x2][y2] - preSum[x2][y1-1] - preSum[x1-1][y2] + preSum[x1-1][y1-1]
    print(answer)