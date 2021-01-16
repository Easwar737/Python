"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?"""

# I have manually given the input. This one works perfectly for other testcases too.

j=0
nums=[2,2,1]
for i in nums:
    j=j^i
return j