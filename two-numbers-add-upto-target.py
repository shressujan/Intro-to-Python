class Solution:
    """You are given a list of numbers, and a target number k.
     Return whether or not there are two numbers in the list that add up to k.
     Try to do it in a single pass of the list."""
    @staticmethod
    def two_sum(num_list, target):
        for x in num_list:
            difference = target - x
            if difference in num_list:
                return True

        return False


if __name__ == '__main__':
    print(Solution().two_sum([4, 7, 1, -3, 2], 5))
