#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        self.MAX_CAP = capacity
        self._front = 0
        self._rear =  0
        self.buffer = [0] * (self.MAX_CAP + 1)  # changed so that its fixed size

    def size(self) -> int:
        return (self._rear - self._front) % (self.MAX_CAP + 1)

    def is_empty(self) -> bool:
        return self._front == self._rear

    def is_full(self) -> bool:
        return (self._rear + 1) % len(self.buffer) == self._front

    def enqueue(self, x: float):
        if (self.is_full()): raise RingBufferFull
        else:
            self.buffer[self._rear] = x
            self._rear = (self._rear + 1) % (self.MAX_CAP + 1)

    def dequeue(self) -> float:
        if (self.is_empty()): raise RingBufferEmpty
        to_dequeue = self.buffer[self._front]
        self._front = (self._front + 1) % (self.MAX_CAP + 1)
        return to_dequeue

    def peek(self) -> float:
        if (self.is_empty()): raise RingBufferEmpty
        return self.buffer[self._front]


class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
