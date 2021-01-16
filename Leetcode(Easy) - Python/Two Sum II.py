"""Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice."""

# I have manually given the input. This one works perfectly for other testcases too.

numbers=[2,7,11,15]
target=9
i=0
j=len(numbers)-1
while i<j:
    total=numbers[i]+numbers[j]
    if(total==target):
        return [i+1,j+1]
    elif(total<target):
        i+=1
    else:
        j-=1