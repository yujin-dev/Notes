class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
Recursive - binary of size len from Inorder traversal and Preorder traversal
"""
def buildTree(inOrder:list, preOrder:list, start, end):
    if(start>end):
        return None
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if start == end:
        return tNode
    rootIndex = search(inOrder, start, end, tNode.data)

    tNode.left = buildTree(inOrder, preOrder, start, rootIndex-1)
    tNode.right = buildTree(inOrder, preOrder, rootIndex+1, end)
    return tNode

def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)

inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)

print("Inorder traversal of the constructed tree is ")
inorder(root)