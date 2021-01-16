"""Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself."""

# I have manually given the input. This one works perfectly for other testcases too.


digits=[1,2,3]
if(digits[-1]<9):
    digits[-1]+=1
else:
    if len(digits)==1:
        digits=[1,0]
    else:
        digits=self.plusOne(digits[:-1])+[0]
return digits