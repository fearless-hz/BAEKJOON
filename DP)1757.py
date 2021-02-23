n,m= map(int,(input().split()))
dp = [[[0]*2 for _ in range(m+5)] for i in range(n+5)]
arr=[0]*10001
for i in range(1,n+1):
    arr[i]=int(input())

for i in range(1,n+1):
    for j in range(m+1):
        if j!=1 :
            if(j==0) :
                dp[i][j][0] = max(dp[i - 1][j + 1][0], dp[i - 1][j][0], dp[i - 1][j + 1][1])
            else:
                dp[i][j][1] = dp[i - 1][j - 1][1] + arr[i]
                dp[i][j][0] = max(dp[i - 1][j + 1][1], dp[i - 1][j + 1][0])

        else:
            dp[i][j][1] = dp[i - 1][j - 1][0] + arr[i]
            dp[i][j][0] = max(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])


print(dp[n][0][0])