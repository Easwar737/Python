"""Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. 
In this scenario, how would you change your code?
Credits:
Special thanks to @pbrother for adding this problem and creating all test cases."""


# I have manually given the input. This one works perfectly for other testcases to

s="abc"
t="ahbgdc"
if s==t:
    return 1
else:
    i=0
    j=0
    new_string=""
    while i<len(s) and j<len(t):
        if(s[i] is t[j]):
            new_string+=s[i]
            i+=1
            j+=1
        else:
            j+=1
    return s==new_string