m, n = map(int, input().split())
l = list(map(int, input().split()))

low = 1
high = 1000000001
result = 0

while low <= high:
    mid = (low + high) // 2
    total = 0
    for i in range(len(l)):
        total += l[i] // mid

    if total < m:
        high = mid - 1
    else:
        result = mid
        low=mid+1

print(result)