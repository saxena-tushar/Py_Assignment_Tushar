
# Here is the corrected code I decoded using a binary search tree (BST) as a reference.

from typing import Optional

class Node:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end
        self.left_child: Optional[Node] = None
        self.right_child: Optional[Node] = None

    def insert(self, node: 'Node') -> bool:
        # Correct logic to check for overlap
        if node.end <= self.start:
            # Go to the left subtree
            if self.left_child is None:
                self.left_child = node
                return True
            return self.left_child.insert(node)
        elif node.start >= self.end:
            # Go to the right subtree
            if self.right_child is None:
                self.right_child = node
                return True
            return self.right_child.insert(node)
        else:
            # Overlap detected
            return False


class Calendar:
    def __init__(self):
        self.root: Optional[Node] = None

    def book(self, start: int, end: int) -> bool:
        new_node = Node(start=start, end=end)
        if self.root is None:
            self.root = new_node
            return True
        return self.root.insert(new_node)

