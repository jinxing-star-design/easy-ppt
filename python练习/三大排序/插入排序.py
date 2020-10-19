#比较优化的一种方法
num = [9, 6, 7, 1, 3]
nums = [0] + num
length = len(nums)
counter_swap = 0
counter_iter = 0
for i in range(2, length):
    nums[0] = nums[i]
    j = i-1
    counter_iter += 1 #趟数
    if nums[j] > nums[0]:  #升序排列情况下，哨兵没有被比较数字大，被比较数字就往后移动一位
#哨兵最后放置到最后与它比较的数字之后一个位置上。
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]
            j -= 1
            counter_swap += 1
        nums[j+1] = nums[0]
print(nums[1:], counter_iter, counter_swap)



