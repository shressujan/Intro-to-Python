class Solution:
    """Given an array of integers in an arbitrary order.
    Return whether or not it is possible to make the array
    non-decreasing by modifying at most 1 element to any value. """
    @staticmethod
    def check_non_decreasing(lst):
        number_to_change = 0
        i = 0
        while i < len(lst) - 1 and number_to_change <= 1:
            if lst[i] > lst[i + 1]:
                number_to_change += 1
            i += 1
        return True if number_to_change <= 1 else False


if __name__ == '__main__':
    print(Solution().check_non_decreasing([13, 4, 7]))
    # True
    print(Solution.check_non_decreasing([5, 1, 3, 2, 5]))
    # False
