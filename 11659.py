import sys
N,M=map(int,sys.stdin.readline().split())
pre=list(map(int,sys.stdin.readline().split()))
answer=0

for i in range(N-1):
    pre[i+1]+=pre[i]

pre=[0]+pre

for i in range(M):
    a,j=map(int,sys.stdin.readline().split())
    answer = pre[j]-pre[a-1]
    print(answer)