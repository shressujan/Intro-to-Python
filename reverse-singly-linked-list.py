class ListNode:
    """
    Given a singly-linked list, reverse the list. This can be done iteratively or recursively.
    Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
    Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL"""

    def __init__(self, x):
        self.val = x
        self.next = None

    def add_item(self, x):
        if self.val is None:
            self.val = x
            return
        while self.next:
            self = self.next
        self.next = ListNode(x)

    def printList(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += ' '
            node = node.next
        print(output)

    @staticmethod
    def reverseIteratively(head):
        current_node = head
        num = 0
        step = 10
        while current_node:
            num = num * step + current_node.val
            current_node = current_node.next

        # Create list
        lst = ListNode(None)
        while num != 0:
            rem = num % step
            lst.add_item(rem)
            num //= step

        return lst

    # def reverseRecursively(self, head, num):
    #     current_node = head
    #     if current_node.next:
    #         num = num * 10 + current_node.val
    #         ListNode.reverseRecursively(self, current_node.next, num)
    #
    #         if self is None:
    #             self.val = current_node.val
    #         else:
    #             self.next = current_node


if __name__ == '__main__':
    # Test Program
    # Initialize the test list:
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail

    print('Initial list: ')
    testHead.printList()

    lst = testHead.reverseIteratively(testHead)
    print('List after reversal: ')
    lst.printList()

    # lst = ListNode(None)
    # lst.reverseRecursively(testHead, 0)
    # print('List after reversal: ')
    # lst.printList()
