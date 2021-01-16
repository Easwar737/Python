"""Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace 
and initial word order."""

# I have manually given the input. This one works perfectly for other testcases too.

s="Let's take LeetCode contest"
list1=s.split(" ")
for i in range(len(list1)):
    temp=list1[i]
    list1[i]=temp[-1::-1]
return " ".join(list1)