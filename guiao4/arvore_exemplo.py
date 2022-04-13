from binarytree import Node

# create root node
root = Node(1)

# create node at connect at left
node2 = Node (2)
root.left = node2

# create other node and connect to root at right
root.right = Node(3)
node8 = root.right

# add nodes to node2
node2.left= Node(4)
node2.right= Node(5)
# keep reference to node with v
node5 = node2.right

# add to node with 5
node5.left = Node(6)

# add using complete path from root
root.right.right = Node(7)
root.right.right.right = Node(8)
root.right.left = Node(9)


# Getting binary tree
print('Binary tree :', root)
 
