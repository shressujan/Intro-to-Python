class Solution:
    """Given a list of numbers, find if there exists a pythagorean triplet in that list.
     A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2"""

    @staticmethod
    def findPythagoreanTriplets(nums):
        # Lets make sure the list of numbers is greater or equal to 3
        if len(nums) < 3:
            return False
        # Lets make sure there are no repetitions in the list
        for x in nums:
            while nums.count(x) > 1:
                nums.remove(x)

        # Sort the list in descending order
        # Quickest way is to use MergeSort with T(n) = nlogn complexity
        nums.sort(reverse=True)

        # Time complexity is O(n^2)
        for i in range(len(nums)):
            start = nums[i]
            for j in range(i+1, len(nums)):
                rem = start**2 - nums[j]**2
                if rem**(1/2) in nums:
                    return True

        return False


if __name__ == '__main__':
    print(Solution().findPythagoreanTriplets([3, 5, 12, 5, 13]))
