"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[i*i for i in nums]
nums.sort()
return nums