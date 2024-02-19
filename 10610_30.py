arr = list(map(str,input()))

if not ('0' in arr):
    print(-1)
elif sum(int(i) for i in arr) % 3 != 0:
    print(-1)
else:
    print(''.join(sorted(arr,reverse=True)))