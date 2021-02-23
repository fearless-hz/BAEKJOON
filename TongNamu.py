import sys
T = int(sys.stdin.readline()) #테스트케이스 개수

for i in range(T):
    N = int(sys.stdin.readline())
    lis = list(map(int,sys.stdin.readline().split()))
    lis.sort()
    score=0
    for j in range(2,N):
        a=abs(lis[j]-lis[j-2])
        score=max(a,score)
    print(score)
