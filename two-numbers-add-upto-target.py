class Solution:
    @staticmethod
    def two_sum(num_list, target):
        for x in num_list:
            difference = target - x
            if difference in num_list:
                return True

        return False


if __name__ == '__main__':
    print(Solution().two_sum([4, 7, 1, -3, 2], 5))
