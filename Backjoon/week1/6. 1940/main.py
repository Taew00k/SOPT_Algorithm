a = int(input())
b = int(input())
nums = list(map(int,input().split()))

nums.sort()
left = 0
right = len(nums) - 1
count = 0

while left < right:
    sum_num = nums[left] + nums[right]
    if sum_num < b:
        left += 1
    elif sum_num > b:
        right -= 1
    else:
        count += 1
        left += 1
        right -= 1

print(count)