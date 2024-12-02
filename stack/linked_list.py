import typing


class StackUnderFlowError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        raise "Stack is empty"


class Node:
    def __init__(self, data: object) -> None:
        self.data = data
        self.next = None
        self.tail = None

    def __repr__(self) -> str:
        return f"{self.data}"


class LinkedListStack:
    def __init__(self) -> None:
        self.head = None


    def push(self, value: object) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def pop(self) -> typing.Optional[object]: # pop by traversal
        if not self.head:
            raise StackUnderFlowError
        if not self.head.next:
            self.head = None
            return
        node = self.head
        while node.next and node.next.next:
            node = node.next
        value = node.next.data
        node.next = None
        return value
    
    
    def peek(self) -> typing.Optional[object]:
        node = self.head
        if not node:
            raise StackUnderFlowError
        while node.next:
            node = node.next
        return node.data


    def search(self, value) -> object:
        node = self.head
        if not node:
            raise StackUnderFlowError
        while node.next:
            if node.data == value:
                return True
            node = node.next
        return False


    def __repr__(self) -> str:
        node = self.head
        str_ = f"{node.data} -> "
        while node.next:
            node = node.next
            str_ += f"{node.data} -> "
        return str_    


if __name__ == "__main__":
    a = LinkedListStack()
    a.push(7)
    a.push(8)
    a.push(89)
    print(a.search(8))
    print(a.search(12))
    print(a)
    print(a.pop())
    print(a)
    print(a.peek())
