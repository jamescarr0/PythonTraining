from collections import defaultdict
from queue import PriorityQueue

class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"


def merge_k_linked_lists(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_k_linked_lists([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''


    val_to_links = defaultdict(list)
    pq = PriorityQueue()

    for link in linked_lists:
        val_to_links[link.val].append(link)
        pq.put(link.val)

    print(val_to_links)
    result = Link(0)
    pointer = result

    # how many times does the while loop run?
    # k*n
    while len(val_to_links) != 0:  # O(1)
        min_val = pq.get()  # O(log(k))
        link = val_to_links[min_val].pop()  # O(1)
        pointer.next = Link(link.val)
        pointer = pointer.next

        if len(val_to_links[min_val]) == 0:
            del val_to_links[min_val]  # O(1)
        if link.next:
            val_to_links[link.next.val].append(link.next)  # O(1)
            pq.put(link.next.val)

    return result.next


ll = [Link(1, Link(2)),Link(2, Link(4)),Link(3, Link(3))]
print(merge_k_linked_lists(ll))