"""The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance."""

# I have manually given the input. This one works perfectly for other testcases too.

x = 1, 
y = 4
return bin(x^y)[2:].count('1')