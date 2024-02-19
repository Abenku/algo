n = int(input())
p = list(map(int,input().split()))
b,c = map(int,input().split())

cnt = n

def cnt_sub(n,c): 
    return n//c if n%c==0 else n//c+1

for i in p:
    if i-b > 0:
        cnt += cnt_sub(i-b,c)
print(cnt)