"""For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2."""

# I have manually given the input. This one works perfectly for other testcases too.

str1 = "ABCABC"
str2 = "ABC"
len1=len(str1)
len2=len(str2)
if str1+str2==str2+str1:
    return str1[:g(len1,len2)]
else:
    return ""
                