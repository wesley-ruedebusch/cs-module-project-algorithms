
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# assume the is always *only one* odd int out

def single_number(arr):
    
    # loop thru array
    # for i in range(length):
    while len(arr) > 1:
        # pop out the last number
        oddity = arr.pop(-1)
        # check if that number is still in the array
        if oddity not in arr:
            # if not return it
            return oddity
        # now remove the non-oddity, or else we'll get a false-positive
        else:
            arr.remove(oddity)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")