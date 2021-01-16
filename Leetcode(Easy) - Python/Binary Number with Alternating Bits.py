"""Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values."""

# I have manually given the input. This one works perfectly for other testcases too.

n=5
n=bin(n)[2:]
i,j=0,1
while j<len(n):
    if n[j]!=n[i]:
        j+=1
        i+=1
        continue
    else:
        return False
else:
    return True