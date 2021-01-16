"""Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, 
find the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'."""

# I have manually given the input. This one works perfectly for other testcases too.

target="a"
letters=["c", "f", "j"]
if target>=letters[-1]:
    return letters[0]
for i in letters:
    if ord(i)>ord(target):
        return i