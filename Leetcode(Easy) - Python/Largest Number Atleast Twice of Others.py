"""In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[3, 6, 1, 0]
if len(nums)<2:
    return nums.index(nums[0])
else:
    val=max(nums)
    pos=nums.index(val)
    nums.remove(val)
    count=0
    for i in nums:
        if i*2<=val:
            count+=1
    if(count is len(nums)):
        return pos
    else:
        return -1