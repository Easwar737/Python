# Here I considered that the list to be checked, as sublist, if the indices of the elements are consecutive.

list1=list(map(int,input("Enter values for MAIN LIST:").split(",")))
pos=[]
def check_sublist(num_list):
    for i in num_list:
        if(i in list1):
            pos.append(list1.index(i))
    flag=0
    for i in range(len(pos)-1):
        if(pos[i]+1==pos[i+1]): 
            flag+=1
        else:
            flag=0
    if flag>0:
        return True
    else:
        return False
        
check_list=list(map(int,input("Enter values to check in MAIN LIST:").split(",")))
result=check_sublist(check_list)
print(result)