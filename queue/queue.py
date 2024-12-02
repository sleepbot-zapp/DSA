class QueueUnderFlowError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        raise "Queue is empty"
    

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


    def __repr__(self) -> str:
        return f"{self.data}"
    

class LinkedListQueue:
    def __init__(self) -> None:
        self.head = None


    def enqueue(self, value):
        if not self.head:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)


    def dequeue(self):
        if not self.head:
            raise QueueUnderFlowError
        prev_node = self.head
        self.head = self.head.next
        return prev_node


    def peek(self):
        if not self.head:
            raise QueueUnderFlowError
        return self.head
 
    
    def __repr__(self) -> str:
        node = self.head
        str_ = f"{node.data} -> "
        while node.next:
            node = node.next
            str_ += f"{node.data} -> "
        return str_   


if __name__ == "__main__":
    l = LinkedListQueue()
    l.enqueue(10)
    l.enqueue(20)
    l.enqueue(30)
    l.enqueue(40)
    print(l)
    print(l.peek())
    print(l.dequeue())
    print(l)
    l.enqueue(90)
    print(l)