class QueueOverFlowError(BaseException):
    def __init__(self, max_size) -> None:
        super().__init__(max_size)
        raise f"Queue is already at is maximum size {max_size}"


class QueueUnderFlowError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        raise "Queue is empty"


class StaticQueue:
    def __init__(self, *args) -> None:
        self._data = list(args)
        self._length = len(self._data)


    def enqueue(self, value):
        if len(self._data) < self._length:
            self._data.append(value)
            return
        raise QueueOverFlowError(self._length)


    def dequeue(self):
        if self._data:
            return self._data.pop(0)
        raise QueueUnderFlowError


    def peek(self):
        if self._data:
            return self._data[0]
        raise QueueUnderFlowError


    def __repr__(self):
        return "<-" + " ".join([str(i) for i in self._data]) + "<-"


class DynamicQueue:
    def __init__(self, *args) -> None:
        self._data = list(args)


    def enqueue(self, value):
        self._data.append(value)


    def dequeue(self):
        if self._data:
            return self._data.pop(0)
        raise QueueUnderFlowError


    def peek(self):
        if self._data:
            return self._data[0]
        raise QueueUnderFlowError


    def __repr__(self):
        return "<-" + " ".join([str(i) for i in self._data]) + "<-"


if __name__ == "__main__":
    queue1 = StaticQueue(1, 2, 3, 4)
    print(queue1)
    print(queue1.dequeue())
    print(queue1)
    queue1.enqueue(4)
    print(queue1)
    print()
    queue2 = DynamicQueue(1, 2, 3, 4)
    print(queue2)
    queue2.enqueue(4)
    print(queue2)   
    print(queue2.dequeue())
    print(queue2)