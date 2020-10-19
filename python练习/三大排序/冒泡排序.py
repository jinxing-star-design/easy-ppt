nums = [1, 8, 7, 6, 9]
length = len(nums)
counter = 0
counter_swap = 0
for i in range(length):
    for j in range(length-i-1):
        counter += 1
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = tmp
            counter_swap += 1
print(nums, counter, counter_swap)
line = [0, 1, 2, 3]