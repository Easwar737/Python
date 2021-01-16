"""Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters."""

# I have manually given the input. This one works perfectly for other testcases too.

s=["h","e","l","l","o"]
s[::1]=s[-1::-1]