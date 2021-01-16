"""Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original."""

# I have manually given the input. This one works perfectly for other testcases too.

s="abcdefg"
k=2
s=list(s)
for i in range(0,len(s),k*2):
    s[i:i+k]=s[i:i+k][::-1]
return "".join(s)
                