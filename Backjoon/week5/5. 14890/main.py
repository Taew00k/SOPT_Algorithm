import sys
input = sys.stdin.readline

N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def can_pass(line):
    used = [False] * N 
    for i in range(1, N):
        if line[i] == line[i - 1]:
            continue 
        elif line[i] - line[i - 1] == 1:
            for j in range(1, L + 1):
                if i - j < 0 or line[i - 1] != line[i - j] or used[i - j]:
                    return False
                used[i - j] = True
        elif line[i - 1] - line[i] == 1:
            for j in range(L):
                if i + j >= N or line[i] != line[i + j] or used[i + j]:
                    return False
                used[i + j] = True
            i += L - 1 
        else:
            return False
    return True

result = 0

for i in range(N):
    if can_pass(grid[i][:]):
        result += 1

for i in range(N):
    column = [grid[j][i] for j in range(N)]
    if can_pass(column):
        result += 1

print(result)