def perfect_square_num(n):
    if n**0.5 == int(n**0.5):
        return True
    else:
        return False   

n = int(input())
m = int(input())

minimum = m
res = 0

for i in range(n,m+1):
    if perfect_square_num(i):
        minimum = min(minimum,i)
        res += i

if res == 0:
    print(-1)
else:
    print(res)
    print(minimum)