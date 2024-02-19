num = int(input())
tmp = num
cnt = 0
check = num - 1

while num != check:
    new = (tmp // 10 + tmp % 10) % 10
    tmp = (tmp % 10) * 10 + new
    cnt += 1
    check = tmp
print(cnt)