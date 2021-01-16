"""Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation."""

# I have manually given the input. This one works perfectly for other testcases too.

num=5
num=bin(num)[2:]
res=""
for i in num:
    if i=="1":
        res+="0"
    else:
        res+="1"
return int(res,2)