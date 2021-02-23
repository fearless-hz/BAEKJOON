cnt = int(input())
time = sorted([tuple(map(int, input().split())) for i in range(cnt)], key = lambda x : (x[1], x[0]))
ans = 0
end = 0
for s, e in time :
    if s>=end :
        ans+=1
        end = e
print(ans)
#정렬 : 1. 끝나는 시간의 오름차순(빨리끝날수록)  2. 시작하는 시간의 오름차순
# EX)cnt=2 / (1 2) (2 2) 로 하면 2번, (2 2) (1 2) 로 하면 1번