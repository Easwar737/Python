"""Given a singly linked list, determine if it is a palindrome."""

curr_node=head
list1=[]
while curr_node:
    list1.append(curr_node.val)
    curr_node=curr_node.next
return list1[::1]==list1[-1::-1]