num_1=int(input("Enter num1:"))
num_2=int(input("Enter num2:"))
def addition(n1,n2):
    while(n2!=0):
        carry=n1&n2
        n1=n1^n2
        n2=carry<<1
    print("Addition:",n1)

def subtraction(a,b):
    while(b!=0):
        borrow=(~a&b)
        a=a^b
        b=borrow<<1
    print("Subtraction:",a)
addition(num_1,num_2)
subtraction(num_1,num_2)