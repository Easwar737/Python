n=int(input("Enter number(of times) to rotate:"))
num_list=list(map(int,input("Enter values for list:").split(",")))
length=len(num_list)
def rotate(n):
    for i in range(n):
        rotate_list()

def rotate_list():
    temp=num_list[0]
    for i in range(length-1):
        num_list[i]=num_list[i+1]
    num_list[length-1]=temp

def print_list():
    print(num_list)

rotate(n)
print_list()
