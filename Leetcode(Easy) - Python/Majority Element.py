"""Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array."""

# I have manually given the input. This one works perfectly for other testcases too

nums=[3,2,3]
if(len(nums)==1):
    return nums[0]
return max(set(nums),key=nums.count)