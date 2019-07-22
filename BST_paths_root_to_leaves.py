# JUNE 29, 2019
# DAILY CODING PROBLEM 110

# DESCRIPTION
# This problem was asked by Facebook.
# Given a binary tree, return all paths from the root to the leaves.

# For the given binary tree:
#            50
#           /  \
#         30    70
#         / \   / \
#       20  40 60 80

# return [[50,30,20], [50,30,40], [50,70,60],[50,70,80]]

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


# The following method follows the BST via Pre-Order Traversal

def pre_order_traversal(node):
    if node is not None:
        print(node.val, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


# Given a binary tree, this method returns all paths from the root to the leaves using pre_order traversal.
def path_root_to_leaves (node, path_list=[]):
    if node is None:
        return

    # Once we visit a node, we append it to the list.
    path_list.append(node.val)
    path_root_to_leaves(node.left, path_list)

    # Once we reach a LEAF NODE, we print the path.
    # leaf node means that the node has no children.
    if node.left is None and node.right is None:
        print(str(path_list)+str(','), end="")

    path_root_to_leaves(node.right, path_list)

    # whenever we leave the node that is a LEAF NODE, we have to pop it from the stack.
    path_list.pop()

# main program
r = Node(50)
insert_node(r, Node(30))
insert_node(r, Node(20))
insert_node(r, Node(40))
insert_node(r, Node(70))
insert_node(r, Node(60))
insert_node(r, Node(80))

# Print In Order Traversal of Binary Search Tree
print('pre_order_traversal')
pre_order_traversal(r)
print('\n')
print('Paths from the root to the leaves')
print("[", end="")
path_root_to_leaves(r)
print(']')


