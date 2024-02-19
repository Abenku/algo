n = int(input())

def is_prime(n):
    tmp = int(n**0.5)
    if n == 1:
        return False
    for i in range(2, tmp+1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    tmp = str(n)[::-1]
    if n == int(tmp):
        return True
    return False
i = n
while True:
    if is_palindrome(i) and is_prime(i):
        print(i)
        break
    i += 1
