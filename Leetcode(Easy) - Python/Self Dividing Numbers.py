"""A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible."""

# I have manually given the input. This one works perfectly for other testcases too.

left=1
right=22
new_list=[]
for i in range(left,right+1):
    if len(str(i))>1:
        temp=i
        flag=0
        while i>0:
            rem=i%10
            if rem!=0 and temp%rem==0 :
                flag+=1
            else:
                flag=0
                break
            i=i//10
        if flag>0:
            new_list.append(temp)
    else:
        new_list.append(i)
return new_list