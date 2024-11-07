import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def search(x, y):
    global size
    if not (0 <= x < m and 0 <= y < n):
        return False
    if grid[x][y] == 0:
        size += 1
        grid[x][y] = 1
        search(x - 1, y)
        search(x, y - 1)
        search(x + 1, y)
        search(x, y + 1)
        return True
    return False


m, n, k = map(int, input().split())
grid = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for row in grid[y1:y2]:
        row[x1:x2] = [1] * (x2 - x1)

regions = []
total = 0
for i in range(m):
    for j in range(n):
        size = 0
        if search(i, j):
            regions.append(size)
            total += 1

print(total)
print(' '.join(map(str, sorted(regions))))
