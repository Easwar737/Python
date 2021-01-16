"""Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function."""

# I have manually given the input. This one works perfectly for other testcases too

arr=[1,0,2,3,0,4,5,0]
i=0
length=len(arr)
while i<len(arr):
    if arr[i] is 0:
        arr.insert(i+1,0)
        i+=2
    else:
        i+=1
del arr[length:]