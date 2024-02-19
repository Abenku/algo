import math

num = int(input())

l = list(list(map(int, input().split())) for _ in range(num))

for x1,y1,r1,x2,y2,r2 in l:  
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    r_dis = r1+r2
    if dis == 0 and r1 == r2:
        print(-1)
    elif r_dis == dis or abs(r1-r2) == dis:
        print(1)
    elif r_dis > dis and abs(r1-r2) < dis:
        print(2)
    else:
        print(0)