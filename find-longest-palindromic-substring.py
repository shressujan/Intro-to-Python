import numpy as np


class Solution:
    @staticmethod
    def longestPalindrome(s):
        substring_link = []
        longest_palindrome = ""
        for i in range(len(s)):
            if s[i] in substring_link:
                substring_link.append(s[i])
                substring_arr = np.array(substring_link)
                indices = np.where(substring_arr == s[i])[0]
                if str(substring_arr[indices[0]::]) == str(substring_arr[:indices[0] - 1: -1]):
                    longest_palindrome = ''.join(substring_arr[indices[0]::])
            else:
                substring_link.append(s[i])

        return longest_palindrome


if __name__ == '__main__':
    word = "bananana"
    print(Solution().longestPalindrome(word))
