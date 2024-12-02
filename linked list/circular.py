class LinkedListUnderFlow(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        raise "LinkedList is empty."


class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return str(self.data)

class CircularSingle:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, val):
        if not self.head and not self.tail:
            self.head = self.tail = Node(val)
            return
        node = self.tail
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.tail.next = self.head
        self.tail.prev = node


    def pop(self):
        if self.head and self.tail:
            self.tail = self.tail.prev
            self.tail.next = self.head
        else:
            raise LinkedListUnderFlow


    def __repr__(self) -> str:
        node = self.head
        str_ = f"{node.data} -> "
        while node.next:
            node = node.next
            str_ += f"{node.data} -> "
            if node is self.head:
                break
        return str_


a = CircularSingle()
a.append(1)
a.append(2)
a.append(3)
print(a)   