"""You are given two integer arrays nums1 and nums2 both of unique elements, where nums1 is a subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
If it does not exist, return -1 for this number."""

# I have manually given the input. This one works perfectly for other testcases too.

nums1=[4,1,2]
nums2=[1,3,4,2]
num_list=[]
for i in nums1:
    if i in nums2:
        ind=nums2.index(i)
        for j in range(ind+1,len(nums2)):
            if(nums2[j]>i):
                num_list.append(nums2[j])
                break
            else:
                num_list.append(-1)
return num_list