class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next


class Solution:
    """You are given two singly linked lists.
    The lists intersect at some node. Find, and return the node.
    Note: the lists are non-cyclical.
    """

    @staticmethod
    def intersection(a, b):
        # loop through first linked list - complexity is O(n)
        connectionMapping = {}
        while a.next:
            connectionMapping[a.val] = a.next
            a = a.next

        # loop through second linked list - complexity is O(n - k), where k is the position of matching node
        while b:
            if b.val in connectionMapping:
                return b
            b = b.next

        return None


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next

    c = Solution().intersection(a, b)
    c.prettyPrint()
    # 3 4
