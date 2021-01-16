arr=list(map(int,input("Enter values:").split(",")))
length=len(arr)
def check_monotonic(arr,length):
    if(all(arr[i]<=arr[i+1] for i in range(length-1)) or all(arr[i]>=arr[i+1] for i in range(length-1))):
        print(True)
    else:
        print(False)
check_monotonic(arr,length)  

