"""Reverse a singly linked list."""

prev_node=None
while head:
    temp=head
    head=head.next
    temp.next=prev_node
    prev_node=temp
return prev_node