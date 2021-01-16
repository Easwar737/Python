"""Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome."""

# I have manually given the input. This one works perfectly for other testcases too.

s="A man, a plan, a canal: Panama"
s=s.lower()
s="".join(i for i in s if i.isalnum())
if(s==s[-1::-1]):
    return True
else:
    return False