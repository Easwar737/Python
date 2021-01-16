"""Given a binary array, find the maximum number of consecutive 1s in this array."""

# I have manually given the input. This one works perfectly for other testcases too.

nums=[1,1,0,1,1,1]
string=""
for i in nums:
    string+=str(i)
return max(map(len,string.split("0")))