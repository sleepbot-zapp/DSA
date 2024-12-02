class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def __repr__(self):
        return f"Node({self.val})"


class BinaryTree:
    def __init__(self):
        self.root = None


    def append(self, val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)


    def _insert(self, root, new_node):
        queue = [root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)


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


if __name__ == "__main__":
    a = BinaryTree()
    import random
    b = list(range(1, 11))
    random.shuffle(b)
    for i in b:
        a.append(i)
    print(a)
