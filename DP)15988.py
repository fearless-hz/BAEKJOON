import sys
T = int(sys.stdin.readline())
dp=[0 for i in range(100001)]
dp[1]=1;dp[2]=2;dp[3]=4
for i in range(4,100001):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    dp[i]%=1000000009
for i in range(T):
    n = int(input())
    print(dp[n])
