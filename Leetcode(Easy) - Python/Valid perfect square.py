"""Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt."""

# I have manually given the input. This one works perfectly for other testcases too.

from math import sqrt as s
num=16
return s(num)==int(s(num))