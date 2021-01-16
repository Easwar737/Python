"""Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The number of elements initialized in nums1 and nums2 are m and n respectively. 
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2."""

# I have manually given the input. This one works perfectly for other testcases too.

nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
n=3
m=3
i=m
j=0
while i<m+n:
    nums1[i]=nums2[j]
    j+=1
    i+=1
nums1.sort()