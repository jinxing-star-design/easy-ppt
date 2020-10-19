nums = [1,9,8,7,5]
nums_counter = 0
nums_iter = 0
length = len(nums)
for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        nums_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j
    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        nums_counter += 1
print(nums,nums_counter,nums_iter)