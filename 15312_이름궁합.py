alph = [3,2,1,2,3,3,2,3,3,2,2,1,2,2,1,2,2,2,1,2,1,1,1,2,2,1]
man = list(map(str,input()))
woman = list(map(str,input()))

answer = []

for i in range(len(man)):
    man[i] = alph[ord(man[i])-65]
    woman[i] = alph[ord(woman[i])-65]
    answer.append(man[i])
    answer.append(woman[i])

while(len(answer) != 2) :
    tmp = []
    for i in range(1,len(answer)):
        tmp.append((answer[i-1]+answer[i])%10)
    answer = tmp

result = "".join(str(i) for i in answer)
print(result)
