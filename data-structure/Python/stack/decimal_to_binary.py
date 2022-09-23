from stack.Stack import Stack

def dtob(decimal, base = 2):
    myStack = Stack()
    while decimal > 0:
        myStack.push(decimal % base)
        decimal //= base # 나머지
    result = ""
    while not myStack.isEmpty():
        result += str(myStack.pop())
    return result

if __name__ == '__main__':
    print(dtob(15))