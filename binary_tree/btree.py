class Node:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []


    def __repr__(self):
        return f"Node(leaf={self.leaf}, keys={self.keys}, children={len(self.children)})"


class BTree:
    def __init__(self, t) -> None:
        self. t = t
        self.root = None
