class Node(object):
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

def printPath(node, path=[]):
    """ path array : root to leaf path """
    if node is None:
        return
    path.append(node.data)
    if (node.left is None) and (node.right is None): # ->leaf node
        print(' '.join([str(i) for i in path if i!=0]))
    else:
        printPath(node.left, path)
        printPath(node.right, path[0:1])

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    printPath(root)
