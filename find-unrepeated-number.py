class Solution:
    """Given a list of numbers, where every number shows up twice except for one number, find that one number
       Find a way to do this using O(1) memory."""
    @staticmethod
    def singleNumber(nums):
        num_to_repition = {}
        for x in nums:
            if x in num_to_repition:
                num_to_repition[x] += 1
            else:
                num_to_repition[x] = 1

        # Solution in constant space using dictionary
        for i in num_to_repition:
            if num_to_repition[i] == 1:
                return i


if __name__ == '__main__':
    print(Solution().singleNumber([4, 3, 2, 4, 5, 3, 2]))
