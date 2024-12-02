class LinkedListUnderFlow(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        raise "LinkedList is empty."

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def __repr__(self) -> str:
        node = self.head
        str_ = f"{node.data} -> "
        while node.next:
            node = node.next
            str_ += f"{node.data} -> "
        return str_   
    
    def pop(self):
        node = self.head
        while node.next and node.next.next:
            node = node.next
        val = node.next
        node.next = None
        return val
    
    def peek(self):
        node = self.head
        while node.next and node.next.next:
            node = node.next
        val = node.next
        return val
    
    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)


a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
print(a)
print(a.peek())
print(a.pop())
print(a)