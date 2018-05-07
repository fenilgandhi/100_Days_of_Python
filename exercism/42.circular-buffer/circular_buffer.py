from collections import deque


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def read(self):
        try:
            return self.buffer.popleft()
        except:
            raise BufferEmptyException("Empty Buffer")

    def write(self, data):
        try:
            self.buffer.insert(self.capacity, data)
        except:
            raise BufferFullException("Buffer is full")

    def overwrite(self, data):
        try:
            self.buffer.insert(self.capacity, data)
        except:
            self.buffer.popleft()
            self.buffer.append(data)

    def clear(self):
        self.buffer.clear()
