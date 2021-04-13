from array.arrays import Array

"""
    Array reverse
"""

def reversingAnArray(start, end , myArray):
    while(start < end):
        myArray[start], myArray[end-1] = myArray[end-1], myArray[start]
        start +=1
        end -=1

if __name__ == "__main__":

    myArray = Array(10)
    myArray.insert(2, 2)
    myArray.insert(3, 1)
    myArray.insert(4, 7)
    print("Arry before reversing: ", myArray)
    reversingAnArray(start=0, end=len(myArray), myArray=myArray)
    print(myArray)