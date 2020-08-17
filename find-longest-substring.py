class Solution:
    """Given a string, find the length of the longest substring without repeating characters.
       Find a solution in linear time O(n)"""
    @staticmethod
    def lengthOfLongestSubstring(s):
        substring_link = {}
        max_length = 0
        for i in range(len(s) - 1):
            if s[i] not in substring_link.keys():
                substring_link[s[i]] = s[i + 1]
            else:
                if max_length < len(substring_link.keys()):
                    max_length = len(substring_link.keys())
                substring_link = {}
        return max_length


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
