import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
stack = []
cnt = [0 for _ in range(N)]

for i in range(N):
   if S[i] == '(':
       stack.append(i)
   else:
       if stack:
           cnt[i] = 1
           cnt[stack[-1]] = 1
           stack.pop()

result = 0
count = 0

for n in cnt:
   if n == 1:
       count += 1
       result = max(result, count)
   else:
       count = 0

print(result)