"""Given a string s consists of some words separated by spaces, return the length of the last word in the string. 
If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only."""

# I have manually given the input. This one works perfectly for other testcases too.

s="Hello World"
if(s.isspace())==True:
    return 0
else:
    string=s.split()
    return len(string[-1])