class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    """Given a linked list of integers, remove all consecutive nodes that sum up to 0."""
    @staticmethod
    def removeConsecutiveSumToZero(node):
        if not node:
            return Node(0)
        cur_val = node.value
        running_sum = cur_val + Solution().removeConsecutiveSumToZero(node.next).value
        if running_sum == 0:
            return Node(0)
        return Node(running_sum)


if __name__ == '__main__':
    node = Node(10)
    node.next = Node(5)
    node.next.next = Node(-3)
    node.next.next.next = Node(-3)
    node.next.next.next.next = Node(1)
    node.next.next.next.next.next = Node(4)
    node.next.next.next.next.next.next = Node(-4)
    node = Solution().removeConsecutiveSumToZero(node)
    while node:
        print(node.value)
        node = node.next
    # 10
