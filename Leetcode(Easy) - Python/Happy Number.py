"""Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not."""

# I have manually given the input. This one works perfectly for other testcases too.

n=19
digits=set()
while n not in digits:
    digits.add(n)
    n=sum(int(i)**2 for i in str(n))
return n==1