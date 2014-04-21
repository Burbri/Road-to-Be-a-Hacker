def fib(n):
    fiblist = (n+1)*[0]
    fiblist[0] = 1
    fiblist[1] = 1
    for i in range(n-2):
        #iterate from 0 to n-3
        fiblist[i+2] = fiblist[i]+fiblist[i+1]
    return fiblist[n-1]
