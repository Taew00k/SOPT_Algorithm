import sys
input = sys.stdin.readline
from collections import deque

n,m= map(int, input().split())
graph = [input() for _ in range(n)]
visit = [[0] * m for _ in range(n)]
direction = [(-1,0), (1,0), (0,-1), (0,1)] 

def solveMiro():
    visit[0][0] = 1
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            
            if(0<= nx < n and 0 <= ny < m) and graph[nx][ny] == '1' and visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))

solveMiro()
print(visit[n-1][m-1])
