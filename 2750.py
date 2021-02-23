N=int(input())
lis=[]
for i in range(N):
    lis.append(int(input()))
lis.sort(reverse=True) #오름차순 시 (), 내림차순 시 reverse=True
for i in range(N):
    print(lis[i])