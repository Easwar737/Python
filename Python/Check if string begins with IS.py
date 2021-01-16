string=input("Enter a string:")
def check_is(string):
    if(string[:2]=="Is"):
        return string
    else:
        return "Is"+string
    
result=check_is(string)
print("The String is:"+result)