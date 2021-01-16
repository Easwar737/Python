"""Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, 
and all letters reverse their positions."""

# I have manually given the input. This one works perfectly for other testcases too.

S="ab-cd"
S=list(S)
i=0
j=len(S)-1
while i<j:
    if S[i].isalpha() and S[j].isalpha():
        S[i],S[j]=S[j],S[i]
    elif S[i].isalpha():
        i-=1
    elif S[j].isalpha():
        j+=1
    i+=1
    j-=1
return ("".join(S))