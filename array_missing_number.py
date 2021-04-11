from arrays import Array

"""
    total_sum 에서 각 숫자를 제외하면서 missing number를 찾는 방식
"""

def findMissing(myArray, n):
    n = n - 1
    totalSum = (n*(n+1)) // 2
    print(f"totalSum = {totalSum}")
    for i in range(0, n):
        totalSum -= myArray[i]
    return totalSum

if __name__ == "__main__":
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    myArray.delete(4, 4)
    print("Original Array: ", Array)
    print("Missing Element: ", findMissing(myArray, len(myArray)))