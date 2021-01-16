"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[1,3,5,6]
target=5
if target in nums:
    return nums.index(target)
else:
    nums.append(target)
    nums.sort()
    return nums.index(target)