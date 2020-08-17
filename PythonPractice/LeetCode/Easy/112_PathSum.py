class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def hasPathSum(root, sum):
        if(not root):
            return False
        
        queue = [(root,root.val)]
        while(queue):
            node, val = queue.pop(0)
            if(node.left == None and node.right == None and val == sum):
                return True
            if(node.left):
                queue.append((node.left,node.left.val + val))
            if(node.right):
                queue.append((node.right,node.right.val + val))
                
        return False

root = Tree(5)
root.left = Tree(4)
root.right = Tree(8)
root.left.left = Tree(11)
root.left.left.left = Tree(7)
root.left.left.right = Tree(12)
root.right.left = Tree(13)
root.right.right = Tree(4)
root.right.right.right = Tree(1)

print(hasPathSum(root,22))