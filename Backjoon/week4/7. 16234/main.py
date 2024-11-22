import sys
from collections import deque

input = sys.stdin.readline

n,l,r=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))


dx=[1,0,-1,0]
dy=[0,1,0,-1]


def bfs(x,y):
    united=[] 
    que=deque()
    que.append((x,y))
    united.append((x,y))

    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                if l<=abs(graph[x][y]-graph[nx][ny])<=r:
                    if visited[nx][ny]==0:
                        visited[nx][ny]=1
                        que.append((nx, ny))
                        united.append((nx,ny))
    return united

res = 0
while True:
    visited=[[0]*(n) for _ in range(n)] 
    flag=0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0: 
                visited[i][j]=1
                country=bfs(i, j)

                if len(country)>1:
                    flag=1
                    total=sum(graph[x][y] for x,y in country)//len(country)
                    
                    for x,y in country:
                        graph[x][y]=total
    if flag==0:
        print(res)
        break
    res+=1