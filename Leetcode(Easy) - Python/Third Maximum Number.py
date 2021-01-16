"""Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[3,2,1]
if len(nums)<=2:
    return max(nums)
else:
    nums=list(set(nums))
    nums.sort(reverse=True)
    if(len(nums)<=2):
        return max(nums)
    else:
        return nums[2]