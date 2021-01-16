"""Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]"."""

# I have manually given the input. This one works perfectly for other testcases too.

address = "1.1.1.1"
string=""
for i in address:
    if i==".":
        string+="[.]"
    else:
        string+=i
return string