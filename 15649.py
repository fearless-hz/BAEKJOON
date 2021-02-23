N, M = map(int, input().split()) #n까지의 자연수 중 m개 뽑기
answer = [0]*9 #출력 위한 리스트
isused = [0]*9 #사용여부 확인 리스트
#level은 꿈의 단계

def solve(level,N,M):
    if level == M: #M단계 꿈이면 출력 후 탈출
        for i in range(M):
            print(answer[i], end=' ')
        print()
        return #탈출
    for i in range(1, N+1): #1부터 N까지 for문 돌림
        if isused[i]: continue #이미 사용된 경우에는 다음 for문 돌림
        isused[i] = True #사용 후 True로 바꿔줌.
        answer[level] = i #answer 꿈단계에 i값 저장
        solve(level + 1,N,M) #재귀함수 호출해서 다음 단계 꿈 진입
        isused[i] = False #초기화 위해 써줌.
solve(0,N,M)