class ListNode:
    """
    Given a singly-linked list, reverse the list. This can be done iteratively or recursively.
    Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
    Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL"""
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += ' '
            node = node.next
        print(output)

    def reverseIteratively(self, head):
        current_node = head
        next_node = head.next
        while next_node is not None:
            # new_next_node = next_node
            # new_next_node.next = current_node
            # new_node = new_next_node
            # next_node = next_node.next
            self.val = next_node
            self.next = current_node
            next_node = next_node.next



    def reverseRecursively(self, head):
        pass


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

    testHead.reverseIteratively(testHead)
    print('List after reversal: ')
    testTail.printList()
