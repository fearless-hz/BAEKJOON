import sys
N = int(sys.stdin.readline())
M=1000-N
cnt=0
lis = [500,100,50,10,5,1]
for i in lis :
    cnt+=M//i
    M%=i

print(cnt)