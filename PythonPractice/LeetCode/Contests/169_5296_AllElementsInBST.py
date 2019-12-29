class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getAllElements(root1, root2):
    arr1 = []
    arr2 = []
    
    if(root1):
        arr1 = inorder(root1,arr1)
    if(root2):
        arr2 = inorder(root2,arr2)
            
    N = len(arr1)
    M = len(arr2)
    
    output = []
    i = 0
    j = 0
    while(i<N and j<M):
        if(arr1[i] <= arr2[j]):
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1

    if(i==N):
        while(j<M):
            output.append(arr2[j])
            j += 1
    else:
        while(i<N):
            output.append(arr1[i])
            i += 1
    
    return output

def inorder(root,arr):
    if(not root):
        return
    inorder(root.left,arr)
    arr.append(root.val)
    inorder(root.right,arr)
    
    return arr

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)

print(getAllElements(root1,root2))