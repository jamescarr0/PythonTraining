# Bubble sort, 'bubbles' / swaps the largest value to the top of the list.

def bubble_sort(nums):
    """
    >>> bubble_sort([5,1,3,2,4])
    [1, 2, 3, 4, 5]
    """

    # O(n^2)
    for i in range(len(nums)): # O(n)
        for j in range(len(nums) - i - 1): #O(n)
            # Subtract 1 each time as the last value is sorted and in place.
            # Slightly optimises the algorithm but still performs at worse O(n)
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
