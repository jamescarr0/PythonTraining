def merge_sort_sublists(left, right):
    left_index = right_index = 0
    sorted_list = []
    while(len(sorted_list) < len(left) + len(right)):
        # If no numbers remain in a sub list, set that side to infinity 
        # This will stop out of bounds index occouring aswell.

        left_num = left[left_index] if left_index < len(left) else float('inf')
        right_num = right[right_index] if right_index < len(right) else float('inf')

        if (left_num < right_num):
            sorted_list.append(left_num)
            left_index += 1
        else:
            sorted_list.append(right_num)
            right_index += 1

    return sorted_list
    
def merge_sort(nums):
    """ 
    >>> merge_sort([5,3,1,2,4])
    [1, 2, 3, 4, 5]
    """

    if len(nums) <= 1:
        return nums
    midpoint = len(nums) // 2
    left_sublist, right_sublist = nums[:midpoint], nums[midpoint:]
    print(left_sublist, right_sublist)
    return merge_sort_sublists(merge_sort(left_sublist), merge_sort(right_sublist))

print(merge_sort([9,3,6,2,7,4,3,2,7,5,4,9,8,4,7,6,2,1]))