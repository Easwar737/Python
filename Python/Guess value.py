class valuesmall(Exception):
    pass
class valuelarge(Exception):
    pass
num=27
while True:
    try:
        value=int(input("Enter value:"))
        if(value<num):
            raise valuesmall
        elif(value>num):
            raise valuelarge
    except(valuesmall):
        print("TOO SMALL")
        print()
    except(valuelarge):
        print("TOO LARGE")
        print()
    except(TypeError,ValueError) as e:
        print(e.__class__)
        print("Try entering even(int) numbers")
        print()
    else:
        print("Booyah!!,","You guessed it Right!!!.")
        break
