from linked_list.singly_linked_list import SinglyLinkedList

def reversedLinkedList(LinkedList):
    previous = None
    current = LinkedList.head
    while(current!=None):
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    LinkedList.head = previous

if __name__ == "__main__":
    myLinkedList = SinglyLinkedList()
    for i in range(10, 0, -1):
        myLinkedList.insertAtStart(i)
    print("Original: ", end = " ")
    myLinkedList.printLinkedList()
    print()
    print("Reversed: ", end = " ")
    reversedLinkedList(myLinkedList)
    myLinkedList.printLinkedList()
