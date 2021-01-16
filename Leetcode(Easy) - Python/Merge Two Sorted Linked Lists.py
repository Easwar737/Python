"""Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists."""


# I have manually given the input. This one works perfectly for other testcases too.

l1=[1,2,4]
l2=[1,3,4]
if(l1 is None):
    return l2
elif(l2 is None):
    return l1
else:
    temp=None
    if(l1.val<l2.val):
        temp=l1
        l1.next=self.mergeTwoLists(l1.next,l2)
    else:
        temp=l2
        l2.next=self.mergeTwoLists(l2.next,l1)
    return temp