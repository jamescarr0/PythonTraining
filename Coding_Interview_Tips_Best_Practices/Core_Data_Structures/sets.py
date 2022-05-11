def count_unique(s):
    """
    Count the number of unique characters in s
    
    >>> count_unique("aabb")
    2

    >>> count_unique("abcdef")
    6
    """

    # O(1) Constant time, set can take an iterable in its constructor.
    return len(set(s))

    # O(1) using set comprehension.
    # return len({c for c in s})

    # O(n * n) = O(n^2)
    # seen_c = []                 # O(1)
    # for c in s:                 # O(n)
    #     if c not in seen_c:     # O(n)
    #         seen_c.append(c)    # O(1)
    # return len(seen_c)          # O(1)