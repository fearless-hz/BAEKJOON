n, m = map(int,input().split())
idx = []
result=[]
for i in range(n):
    idx.append(input())

for i in range(n-7):
    for j in range(m-7):
        num1 = 0
        num2 = 0
        for k in range(i, i+8):
            for s in range(j, j+8):
                if(idx[k][s]=='W'): #가장 왼쪽 위가 White
                    if((k+s)%2==0): num1+=1 #짝수일 시 num1 비용 발생
                    else : num2+=1
                else : #가장 왼쪽 위가 Black
                    if((k+s)%2==0): num2+=1 #짝수일 시 num2 비용 발생
                    else : num1+=1
        result.append(num1)
        result.append(num2)

print(min(result))