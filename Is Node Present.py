from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Binary TreeNode class
class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
  

def isNodePresent(root, x):
    # Write your code here.
    if root == None:
        return 
    if root.data == x:
        return True
    left = isNodePresent(root.left , x)
    right = isNodePresent(root.right , x)
    if left:
        return True
    if right:
        return True
    




















# To build the tree
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)

    if length<=0 or levelorder[0]==-1:
        return None

    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1

        if leftChild != -1:

            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelorder[index]
        index += 1

        if rightChild != -1:

            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

x = int(input())


if isNodePresent(root, x):
    

    print('true')
else:
    print('false')
