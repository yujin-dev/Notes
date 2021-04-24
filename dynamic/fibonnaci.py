import time
def fibonacci(myList, number):
    if myList[number] == None:
        myList[number] = fibonacci(number-1) + fibonacci(number-2)
    return myList[number]

def fibonacciRec(number):
    if number == 1 or number == 0:
        return number
    else:
        return (fibonacciRec(number-1) + fibonacciRec(number-2))

def fib_memoization(n, lookup):
    if n == 0 or n==1:
        lookup[n] = n
    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
        return lookup[n]

