class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def add_items(self, a, b):
        if self.val is None:
            self.val = a
            self.next = Node(b)
            return
        while self.next:
            self = self.next
        self.next = Node(a)
        self.next.next = Node(b)


class Solution:
    """Given two sorted linked lists, merge them in order."""
    @staticmethod
    def mergeTwoLists(a, b):
        lst = Node(None)
        while a and b:
            if a.val > b.val:
                lst.add_items(b.val, a.val)
            if a.val < b.val:
                lst.add_items(a.val, b.val)

            a = a.next
            b = b.next

        return lst

    @staticmethod
    def mergeTwoListsRecursively(a, b, lst):
        if a and b:
            if a.val > b.val:
                lst.add_items(b.val, a.val)
            if a.val < b.val:
                lst.add_items(a.val, b.val)
            Solution().mergeTwoListsRecursively(a.next, b.next, lst)

        return lst


if __name__ == '__main__':
    # Test program
    # 1 -> 3 ->5
    a = Node(1)
    a.next = Node(3)
    a.next.next = Node(5)

    # 2 -> 4 -> 6
    b = Node(2)
    b.next = Node(4)
    b.next.next = Node(6)

    print('Iteratively')
    c = Solution().mergeTwoLists(a, b)
    while c:
        print(c.val, end='')
        c = c.next
    # 1 2 3 4 5 6

    print('\n\nRecursively')

    r = Solution().mergeTwoListsRecursively(a, b, Node(None))
    while r:
        print(r.val, end='')
        r = r.next
    # 1 2 3 4 5 6
