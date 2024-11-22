import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for k in range(n):
    graph.append(list(input()))

res = 0

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    cnt = 0
    visited[y][x] = True
    q = deque()
    q.append((y,x))

    while q:
        (y, x) = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if (0<=ny<n) and (0<=nx<m):
                if graph[ny][nx] == "L" and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    cnt = visited[y][x] + 1
    return cnt-1

for y in range(n):
    for x in range(m):
        if graph[y][x] == "L":
            visited = [[False] * m for _ in range(n)]
            res = max(bfs(y,x), res)

print(res)