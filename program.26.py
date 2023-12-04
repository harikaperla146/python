#WaPp in binary tree to do pre order traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def preOrder(root):
        if root:
            # print the current nodes data
            print(root.data, end=" ")
            preOrder(root.left)
            #recurively traverse the left subtree
            preOrder(root.right)
root = Node(1)
root.right = Node(2)
root.right.right=Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
#calling preorder function to print the preorder traversal
print("Preorder Travesal:", end=" ")
preOrder(root)