"""Given two arrays, write a function to compute their intersection."""

# I have manually given the input. This one works perfectly for other testcases too.

nums1=[1,2,2,1]
nums2=[2,2]
nums1=list(set(nums1).intersection(set(nums2)))
return nums1