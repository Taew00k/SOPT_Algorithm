import sys
from collections import deque
input = sys.stdin.readline

dir = [(0,1),(0,-1),(-1,0),(1,0)]

def bfs():
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    while q:
        r,c = q.popleft()

        for k in range(4):
            nr = r + dir[k][0]
            nc = c + dir[k][1]
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc]: #외부 공기와 맞닿은 치즈의 경우
                if cheese[nr][nc] == 1:
                    visited[nr][nc] = True
                    cheese[nr][nc] = 0
                    cnt += 1
                else:
                    visited[nr][nc] = True
                    q.append((nr,nc))
    ans.append(cnt)
    return cnt
N,M = map(int,input().split())
cheese = [list(map(int,input().split())) for _ in range(N)]
time =0
ans =[]
while True:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break
print(time-1)
print(ans[time-2])