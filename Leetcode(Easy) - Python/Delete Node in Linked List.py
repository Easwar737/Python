"""Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list."""

# I have manually given the input. This one works perfectly for other testcases too.

head=[4,5,1,9]
node=5
node.val=node.next.val
node.next=node.next.next