from binarytree import Node

root = Node(3)

node6 = Node(6)
#left side from node 6
root.left = node6 

node10 = Node(10)

node6.left = node10

node10.left = Node(2)
node10.right = Node(4)

#right side from root 6

node9 = Node(9)

node6.right = node9

node9.left = Node(7)

node9.left.left = Node(11)
node9.left.right = Node(12)

#rigth side of the root
node8 = Node(8)

root.right = node8

node8.right = Node(5)
node8.left = Node(1)
print('Binary tree :', root)
 
