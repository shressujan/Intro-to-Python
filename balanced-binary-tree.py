from collections import deque


class Node:
    """Given a sorted list of numbers, change it into a balanced binary search tree.
     You can assume there will be no duplicate numbers in the list.
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer

    def createBalancedBST(self, nums):
        mi = len(nums) // 2
        median = nums[mi]
        before_list = nums[0: mi]
        after_list = nums[mi + 1: len(nums)]
        if self.value is None:
            self.value = median
        else:
            if median < self.value:
                while self.left is not None:
                    self = self.left
                self.left = Node(median)
                if mi == 1:
                    self = self.left
                    self.left = Node(before_list[0])
                    self.right = Node(after_list[0])
                    return
            else:
                while self.right is not None:
                    self = self.right
                self.right = Node(median)
                if mi == 1:
                    self = self.right
                    self.left = Node(before_list[0])
                    self.right = Node(after_list[0])
                    return

        self.createBalancedBST(before_list)
        self.createBalancedBST(after_list)


if __name__ == '__main__':
    node = Node(None)
    node.createBalancedBST([1, 2, 3, 4, 5, 6, 7])
    print(node.__str__())
    # 4261357
    #   4
    #  / \
    # 2   6
    # / \ / \
    # 1 3 5 7
