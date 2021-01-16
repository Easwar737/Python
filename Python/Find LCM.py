num_1,num_2=int(input("Enter num1:")),int(input("Enter num2:"))
set_1=set()
set_2=set()
for i in range(1,num_1):
    if(num_1%i==0):
        set_1.add(i)
for i in range(1,num_2):
    if(num_2%i==0):
        set_2.add(i)
lcm=(num_1*num_2)/max(set_1&set_2)
print(int(lcm))


