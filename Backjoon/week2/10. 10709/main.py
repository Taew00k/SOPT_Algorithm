import sys
input = sys.stdin.readline

height, width = map(int, input().split())
grid = [list(input().strip()) for _ in range(height)]

result = []
for row in grid:
    counter = -1
    output = []
    for index, cell in enumerate(row):
        if cell == 'c':
            counter = 0
        elif counter != -1:
            counter += 1
        output.append(counter)
    result.append(output)

for row_result in result:
    print(*row_result)