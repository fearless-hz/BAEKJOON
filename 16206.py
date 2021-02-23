N, M=list(map(int,input().split()))
leng=list(map(int,input().split()))
cut= 2.3
order=[]
tens=[]
ans=0
# 10의 배수는 높은 순으로 앞에 둬서 우선적으로 자르도록
# 10 들은 배열에 넣지 않고 그냥 count해서 마지막에 더하기
# 나머지들은 그냥 배열에 넣기
for i in range(N):
    if leng[i]%10==0:
        if leng[i]==10:
            ans+=1
        else:
            tens.append(leng[i])
    else:
        order.append(leng[i])
tens.sort()
tens.extend(order)
order=tens
# cuts가 M을 넘지 않을 때 까지만 자르기
total_cut=0
for i in range(len(order)):
    # 현재 조각에서 필요한 컷 갯수를 미리 계산
    cur_cut=(order[i]-1) // 10
    # 필요한 컷 갯수가 남은 컷 갯수보다 적거나 같다면
    if cur_cut <= M-total_cut:
        total_cut+= cur_cut
        ans+=(order[i] // 10)
    # 필요한 컷 갯수가 남은 컷 갯수보다 많다면
    else:
        ans+= M-total_cut
        total_cut=M
    # total_cut이 M보다 많아지지는 않을 것이므로 등호
    if M==total_cut:
        break
print(ans)