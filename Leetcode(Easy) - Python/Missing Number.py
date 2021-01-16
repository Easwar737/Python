"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?"""


# I have manually given the input. This one works perfectly for other testcases too.

nums=[3,0,1]
return (len(nums)*(len(nums)+1))//2 -sum(nums)