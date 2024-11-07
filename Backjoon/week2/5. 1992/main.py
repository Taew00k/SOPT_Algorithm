import sys
n = int(input())
matrix = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

def compress(x, y, size):
    initial = matrix[x][y] 
    all_same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != initial:
                all_same = False
                break
        if not all_same:
            break

    if all_same:
        print(initial, end="")
    else:
        # 다르면 영역을 4등분하여 처리
        print("(", end="")
        half = size // 2
        compress(x, y, half)  # 왼쪽 위
        compress(x, y + half, half)  # 오른쪽 위
        compress(x + half, y, half)  # 왼쪽 아래
        compress(x + half, y + half, half)  # 오른쪽 아래
        print(")", end="")

compress(0, 0, n)
