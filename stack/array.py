import typing


class StackUnderFlowError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        raise "Stack is empty"


class StackOverFlowError(BaseException):
    def __init__(self, max_size) -> None:
        super().__init__(max_size)
        raise f"Stack is already at is maximum size {max_size}"


class Stack:
    def __init__(self, *args) -> None:
        self._data = list(args)
        self._length = len(self._data)


    def push(self, data) -> None:
        if len(self._data) < self._length:
            self._data.append(data)
            return
        raise StackOverFlowError(self._length)


    def pop(self) -> typing.Optional[object]:
        if self._data:
            return self._data.pop()
        raise StackUnderFlowError
    

    def peek(self) -> typing.Optional[object]:
        if self._data:
            return self._data[-1]
        raise StackUnderFlowError
    

    def __repr__(self) -> str:
        for i in self._data[::-1]:
            print(f"| {i} |".center(10))


if __name__ == "__main__":
    stack = Stack(1, 10000, 3, 400, 5)
    print(stack.peek())
    print(stack)