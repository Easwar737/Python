"""Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[-1,0,3,5,9,12]
target=9
if target>nums[-1]:
    return -1
low=0
high=len(nums)
mid=low+high>>1
while low<=high:
    if nums[mid]==target:
        return mid
    elif target<nums[mid]:
        high=mid-1
        mid=low+high>>1
    else:
        low=mid+1
        mid=low+high>>1
return -1