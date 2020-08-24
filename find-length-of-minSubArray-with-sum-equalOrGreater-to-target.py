class Solution:
    """Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
     of which the sum ≥ s. If there isn't one, return 0 instead."""

    @staticmethod
    def minSubArrayLen(nums, s):
        nums.sort(reverse=True)
        minSubArray = 0
        for i in range(len(nums)):
            if s > 0:
                s = s - nums[i]
                minSubArray += 1
                for j in range(i+1, len(nums)):
                    if nums[j] >= s > 0:
                        s = s - nums[i]
                        minSubArray += 1
                        break
        return minSubArray


if __name__ == '__main__':
    print(Solution().minSubArrayLen([4, 3, 1, 2, 4, 3], 7))
