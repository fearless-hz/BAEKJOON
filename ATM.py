import sys
N = int(sys.stdin.readline())
lis = list(map(int,sys.stdin.readline().split()))
lis.sort()
result=0

for i in range(N):
    for j in range(i+1) :
        result+=lis[j]
print(result)