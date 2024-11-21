N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 초기 max값 계산 (K-1번째까지의 합)
max_sum = sum(arr[:K])

current_sum = max_sum
for i in range(1, N - K + 1):
    current_sum = current_sum - arr[i - 1] + arr[i + K - 1]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)
