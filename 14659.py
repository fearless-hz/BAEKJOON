a=int(input())
lis=list(map(int, input().split()))
maxhill=0
ans=0
cnt=0
cur_max=0 #봉우리의 최대높이
for i in lis:
    if(i >maxhill):
        maxhill=i
        cnt=0
    else : cnt+=1
    ans = max(ans,cnt)
print(ans)


