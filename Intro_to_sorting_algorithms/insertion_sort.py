
def insertion_sort(nums):
    """ 
    >>> insertion_sort([5,3,1,2,4])
    [1, 2, 3, 4, 5]
    """

    for i in range(1, len(nums)):
        current_item = nums[i]
        ptr = i - 1
        while(ptr >= 0 and current_item < nums[ptr]):
            nums[ptr + 1] = nums[ptr]
            ptr-=1
        nums[ptr+1] = current_item
    return nums