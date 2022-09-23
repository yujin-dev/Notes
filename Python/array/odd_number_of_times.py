"""
    XOR : if a==b, 0 else a ??
"""

def print_odd_occurences(array):
    odd = 0

    for element in array:
        odd = odd^element # XOR
    return odd

if __name__ == "__main__":
    myArray = [3, 4, 1, 2, 4, 1, 2, 5, 6, 4, 6, 5, 3]
    print(print_odd_occurences(myArray))
