def dfs(depth,answer,add,sub,mul,div):
    global minimum, maximum

    if depth == n:
        maximum = max(maximum, answer)
        minimum = min(minimum, answer)
        return
    
    if add:
        dfs(depth+1,answer+nums[depth],add-1,sub,mul,div)
    if sub:
        dfs(depth+1,answer-nums[depth],add,sub-1,mul,div)
    if mul:
        dfs(depth+1,answer*nums[depth],add,sub,mul-1,div)
    if div:
        div_r = abs(answer)//nums[depth] if answer >0 else (abs(answer)//nums[depth]) *-1
        dfs(depth+1,int(div_r),add,sub,mul,div-1)

n = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
minimum, maximum = 1e10, -1e10

dfs(1,nums[0],operator[0],operator[1],operator[2],operator[3])
print(maximum)
print(minimum)