"""Write a function that takes a string as input and reverse only the vowels of a string."""

# I have manually given the input. This one works perfectly for other testcases too.

s="hello"
vowels=['a','e','i','o','u','A','E','I','O','U']
i,j=0,len(s)-1
s=list(s)
while i<j:
    if s[i] not in vowels and s[j] not in vowels:
        i+=1
        j-=1
    elif s[i] in vowels and s[j] in vowels:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    elif s[i] not in vowels:
        i+=1            
    else:
        j-=1
return ''.join(s)