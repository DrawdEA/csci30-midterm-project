#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        # TO-DO: implement this
        self.MAX_CAP = capacity
        self._front = 0
        self._rear =  0
        self.buffer = [None] * (self.MAX_CAP + 1)  # changed so that its fixed size

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        # TO-DO: implement this
        return (self._rear - self._front) % (self.MAX_CAP + 1)  

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        # TO-DO: implement this
        return self._front == self._rear 

    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        # TO-DO: implement this
        return (self._rear + 1) % len(self.buffer) == self._front

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        # TO-DO: implement this

        print("to enqueue: ", x, " rear: ", self._rear, " max: ", self.MAX_CAP)
        if (self.is_full()): raise RingBufferFull
        else:
            self.buffer[self._rear] = x
            self._rear = (self._rear + 1) % (self.MAX_CAP + 1)

    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        # TO-DO: implement this
        print("to dequeue: ", self.buffer[self._front], " front: ", self._front, " max: ") # for debugging
        if (self.is_empty()): raise RingBufferEmpty
        temp = self.buffer[self._front]
        print("new front: ", self.buffer[self._front])
        self._front = (self._front + 1) % (self.MAX_CAP + 1)
        return temp

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        # TO-DO: implement this
        # if (self.is_full()): raise RingBufferFull
        if (self.is_empty()): raise RingBufferEmpty
        return self.buffer[self._front]


class RingBufferFull(Exception):
    '''
    The exception raised when the ring buffer is full when attempting to
    enqueue.
    '''
    pass

class RingBufferEmpty(Exception):
    '''
    The exception raised when the ring buffer is empty when attempting to
    dequeue or peek.
    '''
    pass
