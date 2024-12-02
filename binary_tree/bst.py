class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class BST:
    def __init__(self) -> None:
        self.root = None

    def append(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, current, val):
        if val < current.val:
            if not current.left:
                current.left = Node(val)
            else:
                self._insert(current.left, val)
        elif val > current.val:
            if not current.right:
                current.right = Node(val)
            else:
                self._insert(current.right, val)
                    
    def __repr__(self):
        if not self.root:
            return "Empty Tree"
        return self._repr_helper(self.root, "", True)

    def _repr_helper(self, node, indent, last):
        repr_str = ""
        if node:
            repr_str += indent
            if last:
                repr_str += "└── "
                indent += "    "
            else:
                repr_str += "├── "
                indent += "|   "

            repr_str += f"{node.val}\n"
            repr_str += self._repr_helper(node.left, indent, False)
            repr_str += self._repr_helper(node.right, indent, True)
        return repr_str



a = BST()
# import random
# b = list(range(1, 11))
# random.shuffle(b)
# for i in b:
#     a.append(i)
# print(a)
a.append("Binary Tree")
a.append("BTree")
a.append("BST")
print(a)