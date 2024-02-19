def is_prime(n):
    tmp = int(n**0.5)
    for i in range(2, tmp+1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())

for i in range(n, m+1):
    if i == 1:
        continue
    elif is_prime(i):
        print(i)
