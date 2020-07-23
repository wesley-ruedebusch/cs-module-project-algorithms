'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # initalize array to store maximums
    big_max = []
    # loop through array
    for i in range(len(nums)-k+1):
        little_max = None
        # nested loop from arr[i] to arr[i+k]
        for j in range(k):
            # find little_max
            if little_max is None:
                little_max = nums[i]
            if nums[i + j] > little_max:
                little_max = nums[i + j]
        # append max form inner loop to big max array
        big_max.append(little_max)

    return big_max


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
