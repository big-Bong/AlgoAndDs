class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getAllElements(root1, root2):
    arr1 = []
    arr2 = []
    if(not root1 and not root2):
        return []
    if(not root1):
        inorder(root2,arr2)
        return arr2
    if(not root2):
        inorder(root1,arr1)
        return arr1

    inorder(root1,arr1)
    inorder(root2,arr2)
    i = 0
    j = 0
    N = len(arr1)
    M = len(arr2)
    output = []
    while(i < N and j < M):
        if(arr1[i] <= arr2[j]):
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1
    
    while(j<M):
        output.append(arr2[j])
        j += 1

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

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)

print(getAllElements(root1,root2))