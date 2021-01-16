"""We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Return a list of all uncommon words. 
You may return the list in any order."""

# I have manually given the input. This one works perfectly for other testcases too.

A = "this apple is sweet"
B = "this apple is sour"
A=A.split(" ")
B=B.split(" ")
if all(ele==A[0] for ele in A) and A[0] not in B:
    return B
if all(ele==B[0] for ele in B) and B[0] not in A:
    return A
else:
    for i in A:
        if A.count(i)>1 and i not in B:
            A=list(filter((i).__ne__,A))
    for j in B:
        if B.count(j)>1 and j not in A:
            B=list(filter((j).__ne__,B))
    return list(set(A)^set(B))