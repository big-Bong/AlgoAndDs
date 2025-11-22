class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insertLeftNode(self, node):
        self.left = node
    
    def insertRightNode(self, node):
        self.right = node
    

def inorderTraversal(node):
    if(not node):
        return
    if(node.left):
        inorderTraversal(node.left)
    
    print(node.val)

    if(node.right):
        inorderTraversal(node.right)
    
    return

def preorderTraversal(node):
    if(not node):
        return
    print(node.val)

    if(node.left):
        preorderTraversal(node.left)

    if(node.right):
        preorderTraversal(node.right)
    
    return

def postorderTraversal(node):
    if(not node):
        return
    
    if(node.left):
        postorderTraversal(node.left)

    if(node.right):
        postorderTraversal(node.right)
    
    print(node.val)
    
    return

if __name__ == "__main__":
    root = Node(3)
    root.insertLeftNode(Node(7))
    root.insertRightNode(Node(15))
    root.left.insertLeftNode(Node(2))
    root.left.insertRightNode(Node(1))
    root.left.left.insertLeftNode(Node(0))
    root.right.insertLeftNode(Node(6))
    root.right.insertRightNode(Node(12))
    root.right.left.insertLeftNode(Node(13))
    root.right.right.insertRightNode(Node(8))

    postorderTraversal(root)
