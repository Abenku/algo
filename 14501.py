n = int(input())
days = []
pay = []
dp = []

for _ in range(n):
    i,j = map(int,input().split())
    days.append(i)
    pay.append(j)
    dp.append(j)

dp.append(0)

for i in reversed(range(n)):
    if days[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], pay[i]+dp[i+days[i]])

print(dp[0])