class LinkedListUnderFlow(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        raise "LinkedList is empty."


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


    def __repr__(self) -> str:
        return str(self.val)
    

class DoublyLinked:
    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def append_forward(self, val):
        if not self.head and not self.tail:
            self.head = self.tail = Node(val)
            return
        if self.head.next is self.tail:
            self.tail.prev = self.head
        self.head.prev = Node(val)
        self.head, self.head.next = self.head.prev, self.head



    def append_backward(self, val):
        if not self.head and not self.tail:
            self.head = self.tail = Node(val)
            return
        node = self.tail
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.tail.prev = node


    def pop_forward(self):
        if self.head and self.tail:
            val = self.head
            self.head = self.head.next
            return val
        else:
            raise LinkedListUnderFlow


    def pop_backward(self):
        if self.head and self.tail:
            val = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return val
        else:
            raise LinkedListUnderFlow


    def __repr__(self) -> str:
        str_ = "<-> "
        node = self.head
        while node:
            str_ += f"{node} <-> "
            node = node.next
        return str_
    

if __name__ == "__main__":    
    a = DoublyLinked()
    a.append_backward(1) #
    a.append_backward(2)
    a.append_backward(3)
    a.append_backward(4)
    a.append_forward(5)
    a.pop_forward()
    a.pop_backward()
    print(a)

