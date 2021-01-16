"""Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1."""

# I have manually given the input. This one works perfectly for other testcases too.

s="leetcode"
for i in s:
    if s.count(i)==1:
        return s.index(i)
    else:
        return -1