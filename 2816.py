num = int(input())
channel = [input() for _ in range(num)]
idx1, idx2 = channel.index('KBS1'), channel.index('KBS2')

if idx1 > idx2:
    idx2 += 1
print("1"*(idx1)+"4"*(idx1)+"1"*(idx2)+"4"*(idx2-1))