A, B, C = map(int, input().split())

time = [0 for _ in range(101)]
cost = 0

for i in range(3):
    start, end = map(int, input().split())
    for j in range(start, end):
        time[j] += 1
        
for i in range(101):
    if time[i] == 1:
        cost += A*1
    elif time[i] == 2:
        cost += B*2
    elif time[i] == 3:
        cost += C*3

print (cost)