def checkSum(array, sum):

    array = sorted(array)

    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex < rightIndex:
        if (array[leftIndex] + array[rightIndex]== sum):
            return array[leftIndex], array[rightIndex]
        elif (array[leftIndex] + array[rightIndex]<sum):
            leftIndex += 1
        else:
            rightIndex += 1
    return False, False

if __name__ == "__main__":
    myArray = [10, 20, 30, 40, 50]
    sum = 80

    num1, num2 = checkSum(myArray, sum)
    if (num1 and num2):
        print('Array has elements:', num1, 'and', num2, 'with sum:', sum)
    else:
        print('Array doesn\'t have elements with the sum:', sum)