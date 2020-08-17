class ListNode:
    """You are given two linked-lists representing two non-negative integers.
      The digits are stored in reverse order and each of their nodes contain a single digit.
      Add the two numbers and return it as a linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None

    def make_list(self, item):
        if self.val is None:
            self.val = item
            return
        while self.next:
            self = self.next
        self.next = ListNode(item)


class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2, c=0):
        # First List Node
        step_up = 1
        first_num = 0
        while l1:
            first_num += step_up * l1.val
            step_up *= 10
            l1 = l1.next

        # Second List Node
        step_up = 1
        second_num = 0
        while l2:
            second_num += step_up * l2.val
            step_up *= 10
            l2 = l2.next

        sum_total = first_num + second_num
        lst = ListNode(None)
        while sum_total != 0:
            num = sum_total % 10
            lst.make_list(num)
            sum_total //= 10

        return lst


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
