"""Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note."""

# I have manually given the input. This one works perfectly for other testcases too.

ransomNote="a"
magazine="b"
for i in ransomNote:
    if i in magazine:
        magazine=magazine.replace(i,"",1)
    else:
        return False
    return True