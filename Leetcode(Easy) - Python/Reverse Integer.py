"""Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0."""

# I have manually given the input. This one works perfectly for other testcases too.

x=123
if(x<-(pow(2,31)) or x>(pow(2,31)-1)):
    return 0
else:
    length=len(str(x))
    y=str(x)
    if(y[0]=="-"):
        y="-"+y[-1:-(length):-1]
        if(int(y)<-(pow(2,31)) or int(y)>(pow(2,31)-1)):
            return 0
        else:
            return int(y)
    else:
        y=y[::-1]
        if(int(y)<-(pow(2,31)) or int(y)>(pow(2,31)-1)):
            return 0
        else:
            return int(y)