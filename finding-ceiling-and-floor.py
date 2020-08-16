class Solution:
    """Given an integer k and a binary search tree,
     find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k.
      If either does not exist, then print them as None."""
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    @staticmethod
    def findCeilingFloor(root_node, k, floor=None, ceil=None):
        current_node = root_node
        upper_node = root_node
        while current_node is not None:
            # move to the right of the binary search tree
            if current_node.value < k:
                pass
            # move to the left of the binary search tree
            elif current_node.value > k:
                pass
            # don't move anywhere
            else:
                pass

        floor = current_node
        ceil = upper_node
        return floor.value, ceil.value


root = Solution().Node(8)
root.left = Solution().Node(4)
root.right = Solution().Node(12)

root.left.left = Solution().Node(2)
root.left.right = Solution().Node(6)

root.right.left = Solution().Node(10)
root.right.right = Solution().Node(14)

if __name__ == '__main__':
    print(Solution().findCeilingFloor(root, 5))
