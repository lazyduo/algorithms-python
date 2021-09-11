# class Node:
#     def __init__(self, key):
#         self.children = []
#         self.value = key

#     def addChild(self, child):
#         self.children.append(child)

# if __name__ == '__main__':
#     root = Node(0)
#     root.addChild(Node(2))
#     root.addChild(Node(3))

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value),
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.value),
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.right)
        print(root.value),
        postorder_traversal(root.left)

if __name__ == '__main__':
    root = Node(0)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    print('inorder: '),
    inorder_traversal(root)
    print('\npreorder: '),
    preorder_traversal(root)
    print('\npostorder: '),
    postorder_traversal(root)