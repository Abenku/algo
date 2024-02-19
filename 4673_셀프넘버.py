def constructor(n):
    tmp = list(map(str,str(n)))
    return n+sum(map(int,tmp))

arr = [i for i in range(1,10001)]

for i in range(1,10001):
    if constructor(i) in arr:
        arr.remove(constructor(i))

for i in arr:
    print(i)
