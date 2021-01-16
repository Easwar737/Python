text=input("Enter a sentence:")
string_list=text.split(" ")
string_list.sort(reverse=True,key=len)
print("The string with maximum length:"+string_list[0])