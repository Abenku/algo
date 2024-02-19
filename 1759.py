from itertools import combinations as com

def check(word):
    vowel = 'aieou'
    v = 0
    c = 0
    for i in word:
        if i in vowel:
            v+=1
        else:
            c += 1
    return v,c
l,c  = map(int,input().split())
alpha = list(map(str,input().split()))

candi = list(''.join(i) for i in list(com(alpha, l)))
ans = []

for i in sorted(candi):
    v,c = check(i)
    if v >0 and c>1:
       ans.append("".join(sorted(i)))
for j in sorted(ans):
    print(j)