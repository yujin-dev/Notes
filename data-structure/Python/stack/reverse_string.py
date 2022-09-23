from stack.Stack import Stack

def reverse(string):
    myStack = Stack(len(string))
    for i in string:
        myStack.push(i)
    result = ""
    while not myStack.isEmpty():
        result += myStack.pop()
    return result

if __name__ == '__main__':
    print(reverse("omkar"))