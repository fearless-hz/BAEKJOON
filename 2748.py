n=int(input())
fib = [-1 for i in range(100)]

def solve(n):
    if fib[n]!=-1 :
        return fib[n]
    if n<2:
        fib[n]=n
        return fib[n]
    fib[n]=solve(n-1)+solve(n-2)
    return fib[n]



print(solve(n))