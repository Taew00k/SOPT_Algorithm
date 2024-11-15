import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    temp = 0
    for bracket in input().strip():
        if bracket == '(':
            temp += 1
        else:
            temp -= 1

        if temp < 0:
            print('NO')
            break

    if temp == 0:
        print('YES')

    if temp > 0:
        print('NO')