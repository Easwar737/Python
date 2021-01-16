p,r,t=int(input("Enter the principal amount:")),int(input("Enter the rate:")),int(input("Enter the time span:"))
a=p*(1+(r/100))**t
print("Compound Interest:{0:.3f}".format(a-p))