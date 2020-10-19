nums = []
out = None
for i in range(3):
    nums.append(int(input('{} = '.format(i))))
while nums:
    if len(nums) == 1:
        print(nums[0])
        break
    m = max(nums)
    print(m)
    nums.remove(m)
