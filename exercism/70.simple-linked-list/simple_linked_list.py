class Node(object):
    def __init__(self, value):
        self._data = value
        self._next = None

    def value(self):
        return self._data

    def next(self):
        return self._next

    def link(self, address):
        self._next = address

    def __repr__(self):
        return self._data


class LinkedList(object):
    def __init__(self, values=[]):
        self._start = None
        self._tail = self._start
        self._length = 0
        for value in values:
            self.push(value)

    def __iter__(self):
        return self

    def __next__(self):
        next_value = self._start
        while next_value is not None:
            yield next_value
            next_value = next_value.next()
        raise StopIteration("Completed")

    def __len__(self):
        return self._length

    def head(self):
        if self._tail is None:
            raise EmptyListException("Empty List")
        return self._tail

    def push(self, value):
        """
        Simple push operation takes O(1) time
        """
        n = Node(value)
        if self._length >= 1:
            self._tail.link(n)
        else:
            self._start = n
        self._tail = n
        self._length += 1

    def pop(self):
        """
        Simple pop operation takes O(n) time
        """
        if self._length < 1:
            raise EmptyListException
        prev, curr = None, self._start
        while curr != self._tail:
            print(prev, curr, self._tail)
            prev, curr = curr, curr.next()
        self._tail = prev
        self._tail.link(None)
        self._length -= 1

    def reversed(self):
        prev, curr = None, self._start
        while curr is not None:
            temp = curr.next()
            curr.link(prev)
            prev, curr = curr, temp

        self._start, self._tail = self._tail, self._start


class EmptyListException(Exception):
    pass
