"""Given an integer array nums, find three numbers whose product is maximum and return the maximum product."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[1,2,3]
nums.sort(reverse=True)
i=nums[0]*nums[1]*nums[2]
j=nums[-1]*nums[-2]*nums[0]
return max(i,j)
        