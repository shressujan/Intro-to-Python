class Solution:
    @staticmethod
    def singleNumber(nums):
        num_to_repition = {}
        for x in nums:
            if x in num_to_repition:
                num_to_repition[x] += 1
            else:
                num_to_repition[x] = 1

        for i in num_to_repition:
            if num_to_repition[i] == 1:
                return i


if __name__ == '__main__':
    print(Solution().singleNumber([4, 3, 2, 4, 5, 3, 2]))
