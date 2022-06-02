class Stack:
    """ Stack data structure """
    def __init__(self) -> None:
        self._storage = [] # _ prefix == private.

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item

    def __len__(self):
        return len(self._storage)