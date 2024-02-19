from itertools import combinations as com

l = list(int(input()) for _ in range(9))

ans = list(i for i in com(sorted(l),7) if sum(i) == 100)

for i in range(7):
    print(ans[0][i])