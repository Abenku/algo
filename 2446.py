num = int(input())
cnt = 0
for i in range(2*num-1,0,-2):
    print(" "*cnt+"*"*i)
    cnt+=1
cnt -= 2
for i in range(3,num*2+1,2):
    print(" "*cnt+"*"*i)
    cnt-=1