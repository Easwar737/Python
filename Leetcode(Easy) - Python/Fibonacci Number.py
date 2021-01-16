"""The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1."""

# I have manually given the input. This one works perfectly for other testcases too.

n = 2
fibo=[0,1]
if n==0:
    return fibo[0]
elif n==1:
    return fibo[1]
else:
    for i in range(n):
        total=fibo[i]+fibo[i+1]
        fibo.append(total)
    return fibo[-2]