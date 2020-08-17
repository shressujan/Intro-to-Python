class Solution:
    """Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
     valid. An input string is valid if:
    - Open brackets are closed by the same type of brackets.
    - Open brackets are closed in the correct order.
    - Note that an empty string is also considered valid."""

    @staticmethod
    def isValid(string):
        valid_pair = {'(': ')',
                      '{': '}',
                      '[': ']'}

        if len(string) == 0:
            return True

        for i in range(len(string)):
            current_bracket = string[i]
            if current_bracket in valid_pair:
                closing_bracket = valid_pair[current_bracket]
                index_first_closing_bracket = string.find(closing_bracket)
                if index_first_closing_bracket == -1:
                    return False
                else:
                    string = string.replace(current_bracket, '', 1)
                    string = string.replace(closing_bracket, '', 1)
                    return Solution().isValid(string)

            else:
                return False


if __name__ == '__main__':
    print(Solution().isValid('([{}])()'))
    print(Solution().isValid('({[)]'))
    print(Solution().isValid('()(){(())'))
    print(Solution().isValid('[()]{}'))
