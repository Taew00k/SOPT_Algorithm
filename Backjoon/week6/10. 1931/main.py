n = int(input())
tmp = []

for _ in range(n):
    a,b = map(int, input().split())
    tmp.append((a,b))
tmp.sort(key=lambda x: (x[1], x[0])) 

time = 0
count = 0
for i in tmp:
    if i[0] >= time:
        time = i[1]  
        count += 1

print(count)