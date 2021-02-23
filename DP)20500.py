from itertools import combinations
N=int(input())
mod=1000000007
count=0
lis=[]
for i in range(N): #범위:0~N-1
    a=i; b=N-1-a
    if (a+2*b)%3==1 :
        #print(a,b)
        lis=[0]*a
        for j in range(b):
            lis.append(1) #[1 for i in range(a)]
        #print(lis)
        count+=len(list(combinations(lis,a)))
        #print(count)


print(count%mod)