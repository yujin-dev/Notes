"""
- Input: root node, key
- Output: predecessor node, successor node
    1. if root is null, return None
    2. if key is found,
        2-1) left subtree is not null, predecessor -> right
        2-2) right subtree is not null, successor -> left
    3. key is smaller, root node
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def findPredecessorAndSuccessor(self, data):
        global predecessor, successor
        predecessor = None
        successor = None

        if self is None:
            return

        if self.data == data:
            # maximum value in the left subtree = predecessor
            if self.left is not None:
                temp = self.left
                if temp.right is not None:
                    while(temp.right):
                        temp = temp.right
                predecessor = temp

            #minimum value in the right subtree = successor
            if self.right is not None:
                temp = self.right
                while(temp.left):
                    temp = temp.left
                successor = temp
            return

        if data < self.data:
            print("Left")
            self.left.findPredecessorAndSuccessor(data)
        else:
            print("Right")
            self.right.findPredecessorAndSuccessor(data)

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data: # data가 기존data보다 작으면 left insert
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

if __name__ == '__main__':
    root = Node(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)
    root.findPredecessorAndSuccessor(50)
    if (predecessor is not None) and (successor is not None):
        print("Predecessor: ", predecessor.data, "Successor: ", successor.data)
    else:
        print("Predecessor: ", predecessor, "Successor: ", successor)