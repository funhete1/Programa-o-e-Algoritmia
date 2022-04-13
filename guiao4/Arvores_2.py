from binarytree import *

#parte 2 do exercicio 1 

def main():
    root = Node(3)

    node6 = Node(6)
    #left side from node 6
    root.left = node6 

    node10 = Node(10)

    node6.left = node10

    node10.left = Node(2)
    node10.right = Node(4)

    #right side from root 6
    node6.right = Node(7)

    node6.right.left = Node(11)
    node6.right.right = Node(12)

    #rigth side of the root
    node8 = Node(8)

    root.right = node8

    node8.right = Node(5)
    node8.left = Node(1)
    print('Binary tree :', root)


    


if __name__=="__main__":
    main()

