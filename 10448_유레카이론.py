from itertools import combinations_with_replacement as com

eureka = [1]
for i in range(2,50):
    eureka.append(i+eureka[i-2])

n = int(input())
arr = [int(input()) for _ in range(n)]


for i in arr:
    ans = False
    for j in com(eureka,3):
        if sum(j) == i:
            print(1)
            ans = True
            break
    if not ans:
        print(0)
        
