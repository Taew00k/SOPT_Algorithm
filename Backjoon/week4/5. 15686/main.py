import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

def get_city_chicken_distance(chicken_comb):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in chicken_comb:
            min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
        total_distance += min_distance
    return total_distance

min_chicken_distance = float('inf')
for chicken_comb in combinations(chickens, m):
    min_chicken_distance = min(min_chicken_distance, get_city_chicken_distance(chicken_comb))

print(min_chicken_distance)