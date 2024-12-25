n = int(input())

start = 64
ans = 0
while n:
    if start <= n:
        n -= start
        ans+=1
    start //= 2
print(ans)