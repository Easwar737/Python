"""Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node."""

# I have manually given the input. This one works perfectly for other testcases too.

head=[1,2,3,4,5]
length=0
curr_node=head
while curr_node!=None:
    length+=1
    curr_node=curr_node.next
if length%2==0:
    curr_node=head
    prev_node=head
    ind=length>>1
    i=0
    while curr_node!=None:
        if i==ind:
            return prev_node
        else:
            i+=1
            curr_node=curr_node.next
            prev_node=curr_node
                    
        else:
            ind=t(length/2)
            i=0
            curr_node=head
            prev_node=head
            while curr_node!=None:
                if i==ind:
                    return prev_node
                else:
                    i+=1
                    curr_node=curr_node.next
                    prev_node=curr_node