"""Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[0,1,0,3,12]
for i in nums:
    if i==0:
        nums.append(i)
        nums.remove(i)