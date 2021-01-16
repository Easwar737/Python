"""Given two arrays, write a function to compute their intersection."""

# I have manually given the input. This one works perfectly for other testcases too.

temp=[]
nums1=[1,2,2,1]
nums2=[2,2]
for i in nums1:
    if i in nums2:
        temp.append(i)
        nums2.remove(i)
return temp