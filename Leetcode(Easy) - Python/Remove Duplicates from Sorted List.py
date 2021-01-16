"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well."""

# I have manually given the input. This one works perfectly for other testcases too.

head=[1,1,2]
curr_node=head
if(head==None):
    return head
while(curr_node.next!=None):
    next_node=curr_node.next
    if(next_node.val==curr_node.val):
        curr_node.next=next_node.next
        next_node.next=None
    else:
        curr_node=curr_node.next
return head
