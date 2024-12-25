n = int(input())
order = []

for _ in range(n):
    a, b = map(int, input().split())
    order.append((a, b))
order.sort()

time = 0
for i in order:
    if time < i[0]:
        time = i[0] + i[1]
    else:
        time += i[1]
print(time)