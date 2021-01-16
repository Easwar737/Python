"""Remove all elements from a linked list of integers that have value val."""


curr_node=head
prev_node=None
while(curr_node!=None):
    if(curr_node.val is val):
        if(curr_node==head):
            head=head.next
            curr_node=head
        else:
            prev_node.next=curr_node.next
            curr_node=curr_node.next
    else:
        prev_node=curr_node
        curr_node=curr_node.next
return head