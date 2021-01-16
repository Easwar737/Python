"""Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,and it should return false if every element is distinct."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[1,2,3,1]
return len(nums)>len(set(nums))