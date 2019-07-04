# JULY 3, 2019
# DAILY CODING PROBLEM 107

# DESCRIPTION
# This problem was asked by Microsoft.
# Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

# The following is the definition of the node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# The following method inserts a node into the Binary Search Tree, given the root of the BST.
def insert_node(root, node):
    if root is None:
        root = node

    elif root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert_node(root.right, node)

    elif root.left is None:
        root.left = node

    else:
        insert_node(root.left, node)


# The following method follows the BST via In Order Traversal
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        # Print all node values from BST in a single line.
        print node.val,
        in_order_traversal(node.right)


# main program

if __name__ == "__main__":
    r = Node(50)
    insert_node(r, Node(30))
    insert_node(r, Node(20))
    insert_node(r, Node(40))
    insert_node(r, Node(70))
    insert_node(r, Node(60))
    insert_node(r, Node(80))

    # Print In Order Traversal of Binary Search Tree
    in_order_traversal(r)
