class Solution:
    @staticmethod
    def sortNums(nums):
        num_repition = {}
        for x in nums:
            if x in num_repition:
                num_repition[x] += 1
            else:
                num_repition[x] = 1

        keys = list(num_repition.keys())

        minimum = keys[0]
        for key in keys:
            if minimum > key:
                minimum = key
        keys.remove(minimum)

        maximum = keys[0]
        for key in keys:
            if maximum < key:
                maximum = key
        keys.remove(maximum)

        # The only remaining key is the middle in the list
        middle = keys[0]

        first_list = [minimum] * num_repition[minimum]
        middle_list = [middle] * num_repition[middle]
        last_list = [maximum] * num_repition[maximum]

        new_list = first_list + middle_list + last_list

        return new_list


if __name__ == '__main__':
    print(Solution().sortNums([3, 3, 2, 1, 3, 2, 1]))
