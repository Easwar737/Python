num_list=list(map(int,input("Enter values for list:").split(",")))
j=2
for i in range(len(num_list)):
    if(j==len(num_list)):
        print(num_list.pop(j))
        j=j-(j-2)
    elif(j>len(num_list)):
        j=j-len(num_list)
        if(j>len(num_list)):
            j=(j-len(num_list))-1
            print(num_list.pop(j))
        else:
            print(num_list.pop(j))
            j=j+2
    else:
        print(num_list.pop(j))
        j=j+2