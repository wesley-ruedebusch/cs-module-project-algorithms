'''
Input: a List of integers
Returns: a List of integers
'''
# order of non-zero integers doesn't matter
def moving_zeroes(arr):
    length = len(arr)
    count = 0
    # remove ALL zeros AND append new ones on the end
    while (arr.count(0) and count < length):
        arr.remove(0)
        count += 1
        arr.append(0)
    ## moved this up to the while loop
    # append zeros onto the end
    # for i in range(count):
    #     arr.append(0)
    # return the array    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")