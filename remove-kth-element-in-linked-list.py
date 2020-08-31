class Node:
    """You are given a singly linked list and an integer k.
     Return the linked list, removing the k-th last element from the list.
     Try to do it in a single pass and using constant space."""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

    def removeKthElementFromLinkedList(self, head, k):
        while head:
            if head.val != k:
                if self.val is None:
                    self.val = head.val
                else:
                    while self.next:
                        self = self.next
                    self.next = Node(head.val)
            head = head.next


if __name__ == '__main__':
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    print(head)
    # [1, 2, 3, 4, 5]
    newLinkedList = Node(None)
    newLinkedList.removeKthElementFromLinkedList(head, 3)
    print(newLinkedList)
    # [1, 2, 4, 5]
