"""Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique."""

# I have manually given the input. This one works perfectly for other testcases too.

S="abbaca"
no_dup=[]
for i in S:
    no_dup.append(i)
    if len(no_dup)>1 and no_dup[-1]==no_dup[-2]:
        no_dup.pop()
        no_dup.pop()
return "".join(no_dup)