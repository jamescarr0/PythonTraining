from collections import Counter

def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    '''

    # Empty list, return empty list.
    if not lst: 
        return []
    
    # Unpack returned list[(tuple)] - [(<Top Element>, <Frequency>)]
    top_element, freq = Counter(lst).most_common(1)[0]
    return [i for i, e in enumerate(lst) if e == top_element and freq > len(lst) // 2] # O(n)


res = majority_element_indexes([1, 1, 2])
print(res)