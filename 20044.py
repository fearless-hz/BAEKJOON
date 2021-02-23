n=int(input())
lis2=[]
lis=list(map(int, input().split()))
lis.sort()
for i in range(n):
    result= lis[i]+lis[-1-i]
    lis2.append(result)
print(min(lis2))